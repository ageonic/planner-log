from flask import Blueprint, request
from flask_restful import Api, Resource
from models import User

# initialize blueprint
bp = Blueprint("auth", __name__)
api = Api(bp)


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
                        "token": user.generate_auth_token(10).decode(),
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
