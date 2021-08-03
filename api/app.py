from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# initialize global extensions
db = SQLAlchemy()
migrate = Migrate()

from config import config_map, default_config_name


def create_app(config_name=default_config_name):
    # initialize the flask app
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    # initialize flask extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # register flask blueprints
    from task.routes import bp

    app.register_blueprint(bp, url_prefix="/api/task")

    return app
