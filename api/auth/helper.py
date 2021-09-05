from functools import wraps
from flask import g, request
from models import User


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization", None)
        if auth_header:
            auth_type = auth_header.split()[0]
            token = auth_header.split()[1]
            if auth_type == "Bearer":
                g.user = User.verify_auth_token(token)

                if g.user is None:
                    return {
                        "status": "fail",
                        "message": "invalid or expired token",
                    }, 401

                return f(*args, **kwargs)

    return wrapper
