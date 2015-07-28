from flask.helpers import url_for
from app import app, csrf,login_manager
from flask import render_template, session,request ,redirect
import random
from flask.ext.login import login_user , logout_user ,  login_required
from datetime import datetime

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
