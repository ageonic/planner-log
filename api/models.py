from datetime import datetime, timezone
from sqlalchemy import MetaData

from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import (
    TimedJSONWebSignatureSerializer as Serializer,
    BadSignature,
    SignatureExpired,
)


# naming convention definitions for the db
# this helps prevent errors during db migrations
metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

# initialize the flask-sqlalchemy extension
# the extension is bound to the flask app in app.py
# it is initialized here to prevent circular dependency between app.py and models.py
db = SQLAlchemy(metadata=metadata)


class User(db.Model):
    """User model for storing details about a user"""

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

    tasks = db.relationship("Task", backref=db.backref("user"), lazy=True)
    task_statuses = db.relationship("TaskStatus", backref=db.backref("user"), lazy=True)

    def __init__(self, username, password) -> None:
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.created_date = datetime.now(tz=timezone.utc)

    def __repr__(self):
        return "<User {}>".format(self.username)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expiration):
        serializer = Serializer(current_app.config["SECRET_KEY"], expires_in=expiration)
        return serializer.dumps({"user_id": self.id})

    @staticmethod
    def verify_auth_token(token):
        serializer = Serializer(current_app.config["SECRET_KEY"])
        try:
            data = serializer.loads(token)
            return User.query.get(data["user_id"])
        except BadSignature:
            return None
        except SignatureExpired:
            return None


class DailyEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    task_entries = db.relationship(
        "DailyTaskEntry", backref=db.backref("daily_entry"), lazy=True
    )


class DailyTaskEntry(db.Model):
    daily_entry_id = db.Column(db.ForeignKey("daily_entry.id"), primary_key=True)
    task_id = db.Column(db.ForeignKey("task.id"), primary_key=True)
    complete = db.Column(db.Boolean, default=False, nullable=False)


class TaskStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(32), nullable=False)
    color = db.Column(db.String(16), default="green", nullable=False)
    is_complete = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    tasks = db.relationship("Task", backref=db.backref("status"), lazy=True)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    label = db.Column(db.String(32), nullable=False)


task_tag = db.Table(
    "task_tag",
    db.Model.metadata,
    db.Column("task_id", db.ForeignKey("task.id")),
    db.Column("tag_id", db.ForeignKey("tag.id")),
)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    status_id = db.Column(db.Integer, db.ForeignKey("task_status.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("task.id"))
    created_date = db.Column(db.DateTime, nullable=False)

    subtasks = db.relationship(
        "Task",
        backref=db.backref("parent", remote_side=[id]),
        lazy=True,
        cascade="all,delete",
    )

    tags = db.relationship("Tag", secondary=task_tag)

    daily_task_entries = db.relationship(
        "DailyTaskEntry", backref=db.backref("task"), lazy=True
    )

    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)
        self.created_date = datetime.now(tz=timezone.utc)

    def __repr__(self):
        return "<Task {}:{}>".format(self.id, self.name)

    def owned_by_user(self, user_id):
        """Determines whether the current task is related to the specified user"""
        return self.user_id == user_id
