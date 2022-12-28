from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class BaseConfig:
    APP_NAME = "Solicitor"
    FLASK_APP = environ.get("FLASK_APP")
    FLASK_ENV = environ.get("FLASK_ENV")
