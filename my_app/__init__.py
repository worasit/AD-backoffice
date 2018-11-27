from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Environment, PackageLoader, select_autoescape

from my_app.auth.views import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'database.sqlite'
app.config['WTF_CSRF_SECRET_KEY'] = 'someprivatestringhere'
app.config['LDAP_PROVIDER_URL'] = 'ldap://ldap.forumsys.com:389'
app.config['LDAP_PROTOCOL_VERSION'] = 3

env = Environment(
    loader=PackageLoader('my_app', 'templates'),
    autoescape=select_autoescape(['html'])
)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
app.register_blueprint(auth)

# from my_app.auth.models import User
#
# db.create_all()
