import os

# load environment variables
from dotenv import load_dotenv

load_dotenv()

# get absolute path to project directory
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base configuration options for the flask app.
    See https://flask.palletsprojects.com/en/2.0.x/config/ for details on configuration handling.
    """

    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY", os.urandom(16))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    AUTH_TOKEN_TIMEOUT = int(os.getenv("AUTH_TOKEN_TIMEOUT", 3600))


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "PRODUCTION_DATABASE_URI", "sqlite:///" + os.path.join(basedir, "prod.db")
    )


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "dev.db")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "test.db")


# simple dictionary to help refer to config classes with string names
config_map = {
    "production": ProductionConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}

# the config name that will be used as the default when initializing the app
# set the DEFAULT_CONFIG_NAME environment variable to production for production environments
default_config_name = os.getenv("DEFAULT_CONFIG_NAME", "development")
