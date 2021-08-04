from flask import Blueprint, abort, request
from flask_restful import Api, Resource, fields, marshal_with

from models import db, Task

# initialize blueprint and api
bp = Blueprint("task", __name__)
api = Api(bp)

# objects that will be used to serialize flask-sqlalchemy models
task_serializer = {
    "id": fields.Integer,
    "name": fields.String,
    "complete": fields.Boolean,
    "parent_id": fields.Integer,
}

task_serializer["subtasks"] = fields.Nested(task_serializer)


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


# make routes available to the api
api.add_resource(TaskEntry, "/<int:id>")
