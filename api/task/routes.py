from flask import g, Blueprint, abort, request
from flask_restful import Api, Resource, marshal_with
from auth.helper import token_required
from task.serializers import (
    task_status_serializer,
    task_serializer,
    task_tree_serializer,
)

from models import db, Task, TaskStatus

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
            setattr(task, k, v)

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
        db.session.add(task)
        db.session.commit()
        return task


# make routes available to the api
api.add_resource(TaskStatusList, "/status")
api.add_resource(TaskList, "", "/")
api.add_resource(TaskTree, "/tree/<int:id>")
api.add_resource(TaskEntry, "/<int:id>")
