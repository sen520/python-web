import logging

from flask import Flask
from flask_restx import Api

from settings import Config
from util.log_util import log_config
from util.gpt_util import Chat

log_config(file_path=Config.LOG_PATH, file_name=Config.LOG_NAME,
           maxBytes=1024 * 1024 * Config.LOG_SIZE,
           backupCount=Config.LOG_COUNT,
           LOG_LEVEL=logging.NOTSET)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.chat = Chat(Config.GPT_API_KEY, Config.GPT_MODEL)
    api = Api(app, version='1.0', title='Sample API',
              description='A simple demonstration of a Flask-Restx API',
              )
    return app, api


app, api = create_app()
from apps.user import *
