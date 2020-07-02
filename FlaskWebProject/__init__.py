"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
import logging
import sys


app = Flask(__name__)
app.config.from_object(Config)
app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
app.logger.setLevel(logging.INFO)
Session(app)
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'

import FlaskWebProject.views
