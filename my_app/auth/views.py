from flask import (
    render_template,
    redirect,
    url_for,
    Blueprint,
    g
)
from flask_login import (
    current_user,
    logout_user,
    login_required
)

auth = Blueprint(name='auth', import_name=__name__)


@auth.before_request
def get_current_user():
    g.user = current_user


@auth.route('/')
@auth.route('/home')
def home():
    return render_template('home.html', message='render from auth.home')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.home'))
