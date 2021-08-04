from flask import Blueprint, abort, request
from flask_restful import Api, Resource, fields, marshal_with

from models import db, Task

# initialize blueprint and api
bp = Blueprint("task", __name__)
api = Api(bp)

## objects that will be used to serialize flask-sqlalchemy models

# base representation of a task
task_serializer = {
    "id": fields.Integer,
    "name": fields.String,
    "complete": fields.Boolean,
    "parent_id": fields.Integer,
}

# task along with subtasks
# this includes subtasks for subtasks as well
task_tree_serializer = {k: v for k, v in task_serializer.items()}
task_tree_serializer["subtasks"] = fields.Nested(task_tree_serializer)


class TaskEntry(Resource):
    """Retrieve, update, or delete a single task entry."""

    @marshal_with(task_serializer)
    def get(self, id):
        return Task.query.get_or_404(id)

    @marshal_with(task_serializer)
    def put(self, id):
        task = Task.query.get_or_404(id)
        task.name = request.args.get("name") or task.name
        task.complete = request.args.get("complete") == "1"
        task.parent_id = request.args.get("parent_id") or task.parent_id
        db.session.add(task)
        db.session.commit()
        return task

    def delete(self, id):
        task = Task.query.get_or_404(id)
        db.session.delete(task)
        db.session.commit()
        return "", 201


class TaskTree(Resource):
    """Retrieve a task along with all descendant tasks."""

    @marshal_with(task_tree_serializer)
    def get(self, id):
        return Task.query.get_or_404(id)


# make routes available to the api
api.add_resource(TaskEntry, "/<int:id>")
api.add_resource(TaskTree, "/tree/<int:id>")
