from flask import Blueprint, render_template

NAME = 'BASE'

bp = Blueprint(NAME, __name__)


@bp.route('/')
def index():
    return render_template('index.html')
