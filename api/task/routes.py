from flask import Blueprint

bp = Blueprint("task", __name__)


@bp.route("/")
@bp.route("/all")
def index():
    return {"tasks": ["Do {}".format(i) for i in range(10)]}
