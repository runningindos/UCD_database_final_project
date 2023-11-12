#Import datetime for database entries #

from datetime import datetime

# Connect to Flask #

from flask import Flask, flash, render_template, redirect, request, url_for

#Import login extension for clinician login #
from flask_login import (
    LoginManager,
    login_user,
    logout_user,
    login_required,
    current_user,
)

from models import User, Business, Event, Post, Friendship, Attendance, db


app = Flask(__name__)
app.config.from_object('config')

# Routes for html templates #

@app.route('/')
def home():
    return render_template('index.html')