# from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
# from .models import User
# from . import db   # from init
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import login_user, login_required, logout_user, current_user

# usually easier to keep the name the same as the file
auth = Blueprint('auth', __name__)


# @auth.route('/login', methods=['GET', 'POST'])      # with the methods attribute we are defining the types of requests that it allows (only get by default)
# def login():
#     # we use request to get the data from the form
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             if check_password_hash(user.password, password):
#                 flash('Logged in successfully!', category='success')
#                 login_user(user, remember=True)                       # logs in user, remembers that they're logged in
#                 return redirect(url_for('views.home'))
#             else:
#                 flash('Incorrect password, try again', category='error')
#         else:
#             flash('Email does not exist.', category='error')


#     return render_template("login.html", text="Testing", user=current_user)

# @auth.route('/logout')
# @login_required                    # user needs to be logged in (from flask_login)
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))

# @auth.route('/sign-up', methods=['GET', 'POST'])
# def sign_up():
#     if request.method == 'POST':
#         email = request.form.get('email')
#         first_name = request.form.get('firstName')
#         password1 = request.form.get('password1')
#         password2 = request.form.get('password2')

#         user = User.query.filter_by(email=email).first()
#         if user:
#             flash('There is already an account associated with this email', category="error")
#         elif len(email) < 4:
#             flash('Email must be greater than 3 characters', category="error")
#         elif len(first_name) < 2:
#             flash('First name must be greater than 1 character', category="error")
#         elif password1 != password2:
#             flash('Passwords don\'t match', category="error")
#         elif len(password1) < 7:
#             flash('Password must be greater than 6 characters', category="error")
#         else:
#             # add user to database
#             new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
#             db.session.add(new_user)
#             db.session.commit()
#             login_user(new_user, remember=True)
#             flash('Account created!', category="success")
#             return redirect(url_for('views.home'))             # get the url for the home function in views.py
            
#     return render_template("sign_up.html", user=current_user)