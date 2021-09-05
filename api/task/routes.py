from flask import g, Blueprint, abort, request
from flask_restful import Api, Resource, marshal_with
from auth.helper import token_required
from task.serializers import task_serializer, task_tree_serializer

from models import db, Task

# initialize blueprint and api
bp = Blueprint("task", __name__)
api = Api(bp)


def get_task_or_403(task_id):
    """Retrieve a specified task and abort if the task does not belong to the logged in user."""
    task = Task.query.get_or_404(task_id)

    if not task.owned_by_user(g.user.id):
        abort(403, "insufficient access to the requested task")

    return task


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
        return Task.query.filter_by(user_id=g.user.id).all()

    @token_required
    @marshal_with(task_serializer)
    def post(self):
        data = request.get_json()
        task = Task(
            name=data.get("name"),
            parent_id=data.get("parent_id"),
            user_id=g.user.id,
        )
        db.session.add(task)
        db.session.commit()
        return task


# make routes available to the api
api.add_resource(TaskList, "", "/")
api.add_resource(TaskTree, "/tree/<int:id>")
api.add_resource(TaskEntry, "/<int:id>")
