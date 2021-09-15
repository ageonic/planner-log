import click
from flask import Blueprint, request, current_app
from flask_restful import Api, Resource
from models import db, User

# initialize blueprint
bp = Blueprint("auth", __name__)
api = Api(bp)


@bp.cli.command("create")
@click.option("-u", "--username", "username", required=True)
@click.option("-p", "--password", "password", required=True)
def create_user(username, password):
    """Create a user"""
    if User.query.filter_by(username=username).first() is None:
        user = User(username, password)
        db.session.add(user)
        db.session.commit()
        click.echo(
            "\nsuccessfully added user\n\nid: {}\nusername: {}".format(
                user.id, user.username
            )
        )
    else:
        click.echo("\nusername '{}' already exists".format(username))


class UserLogin(Resource):
    """Authenticate a user to the api"""

    def post(self):
        try:
            if request.authorization:
                if (
                    not request.authorization.username
                    or not request.authorization.password
                ):
                    return {
                        "status": "fail",
                        "message": "username and password required",
                    }, 401

                user = User.query.filter_by(
                    username=request.authorization.username
                ).first()

                if user and user.verify_password(request.authorization.password):
                    return {
                        "status": "success",
                        "token": user.generate_auth_token(
                            current_app.config.get("AUTH_TOKEN_TIMEOUT")
                        ).decode(),
                    }, 200
                else:
                    return {
                        "status": "fail",
                        "message": "username or password incorrect",
                    }, 404
        except Exception as e:
            return {"status": "fail", "message": "an unexpected error occurred"}, 500


# make routes available to the api
api.add_resource(UserLogin, "/login")
