
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, File
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

def check_login(username, password):
    user = User.query.filter_by(username=username).first()
    if user:
        if check_password_hash(user.password, password):
            return "200"
        else:
            return "Wrong password!"
    else:
        return "User does not exist!"

def check_signup(email, username, password1, password2):
    user = User.query.filter_by(username=username).first()
    if user:
        return "User already exists!"
    elif len(password1) < 7:
        return "Password too short"
    elif password1 != password2:
        return "Passwords not matching"
    elif len(username) < 3:
        return "Username too short"
    else:
        return 200



@auth.route("/login", methods = ['POST', "GET"])
def login():
    if request.method == "GET":
        return render_template("/Logon/login.html", user=current_user)
    else:
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        loginreq = check_login(username, password)
        if loginreq == "200":
            pass
        else:
            return render_template("/Logon/login.html", problem = loginreq, user=current_user)

        login_user(user, remember=True)

        return render_template("/Container-Pages/main.html", user=current_user)
        
@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template("/Logon/login.html", user = current_user)
        



@auth.route("/signup", methods = ['POST', "GET"])
def signup():
    if request.method == "GET": # GET request = signup form
        return render_template("/Logon/signup.html", user=current_user)
    else: # POST request = Signup-request

        email = request.form.get("email")

        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]

        # Check if credentials are OK

        signupreq = check_signup(email, username, password1, password2)
        if signupreq == 200:
            pass
        else:
            return render_template("/Logon/signup.html", problem = signupreq, user=current_user)

        # Add user

        new_user = User(email = email, username = username, password = generate_password_hash(password1, method = "pbkdf2:sha256"))
        db.session.add(new_user)
        db.session.commit()
        return render_template("/Logon/login.html", user=current_user)




