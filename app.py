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

from models import User


app = Flask(__name__)
app.config.from_object('config')

# Routes for html templates #

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write', methods=['GET'])
def write():
    return render_template('write.html')

@app.route('/read')
def read():
    return render_template('read.html')

@app.route('/register')
def register():
    return render_template('register.html', methods=['GET', 'POST'])

@app.route('/login')
def login():
    return render_template('login.html', methods=['GET', 'POST'])

