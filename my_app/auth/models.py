import sqlite3

from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired

from my_app import db, app


def get_db_connection():
    connection = sqlite3.connect(app.config['SQLALCHEMY_DATABASE_URI'])
    return connection


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    is_admin = db.Column(db.Boolean(False))

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    @staticmethod
    def try_login(username, password):
        pass

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id


class LoginForm(Form):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])
