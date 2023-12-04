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

from models import User, db


app = Flask(__name__)
app.config.from_object('config')

with app.app_context():
    db.init_app(app)
    db.create_all()

# Routes for html templates #

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/write', methods=['GET', 'POST'])
def write():
    return render_template('write.html')



@app.route('/read')
def read():
    return render_template('read.html')

#setting up a user
@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

#function for registering a user to create an account
@app.route('/register', methods=['POST'])
def register_user():
    username = request.form['userName']
    email = request.form['userEmail']
    password = request.form['userPassword']
    if User.query.filter_by(email=email).first():
        flash(f"This email address is taken")
        return redirect('url_for("register")')
    user = User(userName=userName, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return redirect('url_for("index")')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')



