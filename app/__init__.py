
from flask.ext.login import LoginManager
from flask import Flask
login_manager = LoginManager()

app = Flask(__name__)
from flask_wtf.csrf import CsrfProtect

login_manager.init_app(app)
csrf = CsrfProtect()


csrf.init_app(app)

from app import views, models
