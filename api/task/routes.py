from datetime import datetime, timezone
from flask import g, Blueprint, abort, request
from flask_restful import Api, Resource, marshal_with
from auth.helper import token_required
from task.serializers import (
    task_status_serializer,
    task_serializer,
    task_tree_serializer,
)

from models import db, Task, TaskStatus, Tag, TaskClock

# initialize blueprint and api
bp = Blueprint("task", __name__)
api = Api(bp)


def get_task_or_403(task_id):
    """Retrieve a specified task and abort if the task does not belong to the logged in user."""
    task = Task.query.get_or_404(task_id)

    if not task.owned_by_user(g.user.id):
        abort(403, "insufficient access to the requested task")

    return task


class TaskStatusList(Resource):
    """Retrieve a list of all task statuses or create a single task status for the current user."""

    @token_required
    @marshal_with(task_status_serializer)
    def get(self):
        return TaskStatus.query.filter_by(user_id=g.user.id).all()

    @token_required
    @marshal_with(task_serializer)
    def post(self):
        data = request.get_json()
        status = TaskStatus(
            label=data.get("label"),
            color=data.get("color"),
            user_id=g.user.id,
        )
        db.session.add(status)
        db.session.commit()
        return status


class TaskEntry(Resource):
    """Retrieve, update, or delete a single task entry."""

    @token_required
    @marshal_with(task_serializer)
    def get(self, id):
        return get_task_or_403(id)

    @token_required
    @marshal_with(task_serializer)
    def put(self, id):
        data = request.get_json()
        task = get_task_or_403(id)

        for k, v in data.items():
            if k != "tags":
                setattr(task, k, v)

        task.tags = Tag.query.filter(Tag.id.in_(data.get("tags") or [])).all()

        db.session.add(task)
        db.session.commit()
        return task

    @token_required
    def delete(self, id):
        task = get_task_or_403(id)

        db.session.delete(task)
        db.session.commit()
        return "", 201


class TaskTree(Resource):
    """Retrieve a task along with all descendant tasks."""

    @token_required
    @marshal_with(task_tree_serializer)
    def get(self, id):
        return get_task_or_403(id)


class TaskList(Resource):
    """Retrieve a list of all tasks or create a single task for the current user."""

    @token_required
    @marshal_with(task_serializer)
    def get(self):
        base_query = Task.query.filter(Task.user_id == g.user.id)

        accepted_filters = ["parent_id", "status_id"]

        for key in accepted_filters:
            if key in request.args:
                base_query = base_query.filter(
                    getattr(Task, key)
                    == (None if request.args.get(key) == "" else request.args.get(key))
                )

        return base_query.all()

    @token_required
    @marshal_with(task_serializer)
    def post(self):
        data = request.get_json()
        task = Task(
            name=data.get("name"),
            parent_id=data.get("parent_id"),
            status_id=data.get("status_id"),
            user_id=g.user.id,
        )
        task.tags = Tag.query.filter(Tag.id.in_(data.get("tags") or [])).all()
        db.session.add(task)
        db.session.commit()
        return task


class TaskClockToggler(Resource):
    """Start or stop a running clock on a specified task."""

    @token_required
    def post(self, task_id):
        if g.user.has_running_clock():
            user_clock = g.user.get_running_clock()
            if user_clock.task_id != task_id:
                user_clock.stop_time = datetime.now(tz=timezone.utc)
                db.session.add(user_clock)

        task = get_task_or_403(task_id)

        if task.has_running_clock():
            clock = task.get_running_clock()
            clock.stop_time = datetime.now(tz=timezone.utc)
        else:
            clock = TaskClock(task_id=task.id, start_time=datetime.now(tz=timezone.utc))

        db.session.add(clock)
        db.session.commit()

        return {
            "task_id": task.id,
            "clock_id": clock.id,
            "running": task.has_running_clock(),
        }


# make routes available to the api
api.add_resource(TaskStatusList, "/status")
api.add_resource(TaskList, "", "/")
api.add_resource(TaskTree, "/tree/<int:id>")
api.add_resource(TaskEntry, "/<int:id>")
api.add_resource(TaskClockToggler, "/clock/toggle/<int:task_id>")
