from flask_restful import fields

## objects that will be used to serialize flask-sqlalchemy models

# base representation of a task status
task_status_serializer = {
    "id": fields.Integer,
    "label": fields.String,
    "color": fields.String,
    "is_complete": fields.Boolean,
}

# base representation of a task
task_serializer = {
    "id": fields.Integer,
    "name": fields.String,
    "complete": fields.Boolean,
    "description": fields.String,
    "due_date": fields.DateTime,
    "created_date": fields.DateTime,
    "parent_id": fields.Integer,
    "status": fields.Nested(task_status_serializer),
}

# task along with subtasks
# this includes subtasks for subtasks as well
task_tree_serializer = {k: v for k, v in task_serializer.items()}
task_tree_serializer["subtasks"] = fields.Nested(task_tree_serializer)
