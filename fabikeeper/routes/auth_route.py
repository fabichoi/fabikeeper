from flask import Blueprint, render_template, redirect, url_for, flash, session, request
from fabikeeper.forms.auth_form import LoginForm, RegisterForm
from fabikeeper.models.user import User as UserModel
from werkzeug import security

NAME = 'auth'
bp = Blueprint(NAME, __name__, url_prefix='/auth')

from dataclasses import dataclass

USERS = []


@dataclass
class User:
    user_id: str
    user_name: str
    password: str


USERS.append(User('abcd', 'abcd', security.generate_password_hash('1234')))
USERS.append(User('admin', 'admin', security.generate_password_hash('1234')))
USERS.append(User('tester', 'tester', security.generate_password_hash('1234')))


@bp.route('/')
def index():
    return redirect(url_for(f'{NAME}.login'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        password = form.data.get('password')
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            user = user[0]
            if not security.check_password_hash(user.password, password):
                flash('Password is not valid.')
            else:
                session['user_id'] = user_id
                return redirect(url_for('base.index'))
        else:
            flash('User ID is not exists.')
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/login.html', form=form)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    flash('ERROR!!')
    form = RegisterForm()
    if form.validate_on_submit():
        user_id = form.data.get('user_id')
        user_name = form.data.get('user_name')
        password = form.data.get('password')
        repassword = form.data.get('repassword')
        user = [user for user in USERS if user.user_id == user_id]
        if user:
            flash('User ID is already exists.')
            return redirect(request.path)
        else:
            USERS.append(
                User(
                    user_id=user_id,
                    user_name=user_name,
                    password=security.generate_password_hash(password)
                )
            )
            session['user_id'] = user_id
            return redirect(url_for('base.index'))
        return f'{user_id}, {user_name}, {password}, {repassword}'
    else:
        flash_form_errors(form)
    return render_template(f'{NAME}/register.html', form=form)


@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for(f'{NAME}.login'))


def flash_form_errors(form):
    for _, errors in form.errors.items():
        for e in errors:
            flash(e)
