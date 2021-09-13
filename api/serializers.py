from flask_restful import fields

## objects that will be used to serialize flask-sqlalchemy models

# base representation of a tag
tag_serializer = {
    "id": fields.Integer,
    "label": fields.String,
}

# base representation of a task status
task_status_serializer = {
    "id": fields.Integer,
    "label": fields.String,
    "color": fields.String,
    "is_complete": fields.Boolean,
}

# base representation of a task clock
task_clock_serializer = {
    "id": fields.Integer,
    "start_time": fields.String(attribute=lambda c: str(c.start_time)),
    "stop_time": fields.String(
        attribute=lambda c: str(c.stop_time) if c.stop_time else ""
    ),
    "total_time": fields.String(attribute=lambda c: c.total_time().total_seconds()),
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
    "tags": fields.Nested(tag_serializer),
    "clocked_time": fields.Nested(task_clock_serializer),
    "has_running_clock": fields.Boolean(attribute=lambda c: c.has_running_clock()),
    "running_clock_time": fields.Integer(
        attribute=lambda t: t.get_running_clock().total_time().total_seconds()
        if t.has_running_clock()
        else 0
    ),
}

# task along with subtasks
# this includes subtasks for subtasks as well
task_tree_serializer = {k: v for k, v in task_serializer.items()}
task_tree_serializer["subtasks"] = fields.Nested(task_tree_serializer)

# base representation of a daily task entry
daily_task_entry_serializer = {
    "id": fields.Integer,
    "task": fields.Nested(task_serializer),
    "complete": fields.Boolean,
}

# base representation of a daily entry
daily_entry_serializer = {
    "id": fields.Integer,
    "created_date": fields.DateTime,
    "task_entries": fields.List(fields.Nested(daily_task_entry_serializer)),
}
