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
        data = request.get_json()
        task = Task.query.get_or_404(id)

        for k, v in data.items():
            setattr(task, k, v)

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


class TaskList(Resource):
    """Retrieve a list of all tasks or create a single task."""

    @marshal_with(task_serializer)
    def get(self):
        return Task.query.all()

    @marshal_with(task_serializer)
    def post(self):
        data = request.get_json()
        task = Task(
            name=data.get("name"),
            parent_id=data.get("parent_id"),
        )
        db.session.add(task)
        db.session.commit()
        return task


# make routes available to the api
api.add_resource(TaskList, "", "/")
api.add_resource(TaskTree, "/tree/<int:id>")
api.add_resource(TaskEntry, "/<int:id>")
