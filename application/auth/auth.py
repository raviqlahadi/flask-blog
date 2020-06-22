from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from .form import RegisterForm, LoginForm
from passlib.hash import sha256_crypt
from application.model import db, User
from datetime import datetime
from functools import wraps


auth_bp = Blueprint(__name__, 'auth_bp')

@auth_bp.route('/')
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = form.username.data
        password = form.password.data

        curent_user = User.query.filter_by(username=username).first()
        if curent_user is not None:
            upass = curent_user.password
            if sha256_crypt.verify(password, upass):
                session['logged_in'] = True
                session['email'] = curent_user.username
                session['user_name'] = curent_user.name
                curent_user.last_login = datetime.now()
                db.session.commit()
                flash(f'Login success, welcome {curent_user.name}')
                return redirect(url_for('application.dashboard.dashboard.dashboard'))
            else:
                flash('Password is incorent')

        else:
            flash('User not found')

    return render_template('admin/login.html', form=form)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        new_user = User(
            username = form.username.data,
            name = form.name.data,
            password = sha256_crypt.encrypt(str(form.password.data))
         )
        db.session.add(new_user)
        db.session.commit()
        flash('New user registered, now you can login','info')
        return redirect(url_for('application.auth.auth.login'))
    else:
        return render_template('admin/register.html', form=form)

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout succesfull','info')
    return redirect(url_for('application.auth.auth.login'))

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please Login','danger')
            return redirect(url_for('application.auth.auth.login'))

    return wrap