from flask import Flask
from flask_migrate import Migrate

from config import config_map, default_config_name
from models import db

# initialize global extensions
migrate = Migrate()


def create_app(config_name=default_config_name):
    # initialize the flask app
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    # initialize flask extensions with app
    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)

    # register flask blueprints
    from task.routes import bp

    app.register_blueprint(bp, url_prefix="/api/task")

    return app
