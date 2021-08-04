from flask_sqlalchemy import SQLAlchemy

# initialize the flask-sqlalchemy extension
# the extension is bound to the flask app in app.py
# it is initialized here to prevent circular dependency between app.py and models.py
db = SQLAlchemy()


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    complete = db.Column(db.Boolean, default=False, nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey("task.id"))

    subtasks = db.relationship(
        "Task",
        backref=db.backref("parent", remote_side=[id]),
        lazy=True,
        cascade="all,delete",
    )

    def __repr__(self):
        return "<Task {}:{}>".format(self.id, self.name)
