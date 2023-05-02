import os
import sys

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_assets import Environment, Bundle

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(32)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(os.path.dirname(app.root_path), os.getenv('DATABASE_FILE', 'data.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    from VAE_Insight.models import User
    return User.query.get(int(user_id))

assets = Environment()
assets.init_app(app)

with app.app_context():
    from VAE_Insight.dashboard import init_dashboard
    app = init_dashboard(app)

# login_manager.login_view = 'login'

from VAE_Insight import views, errors, commands