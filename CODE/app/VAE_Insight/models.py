from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from VAE_Insight import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, unique=True)
    email = db.Column(db.String(150), unique = True, index = True)
    password_hash = db.Column(db.String(150))
    joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)
    feature1 = db.Column(db.String(150), default = 'None', unique=False)
    feature2 = db.Column(db.String(150), default = 'None', unique=False)
    feature3 = db.Column(db.String(150), default = 'None', unique=False)
    feature4 = db.Column(db.String(150), default = 'None', unique=False)
    feature5 = db.Column(db.String(150), default = 'None', unique=False)
    feature6 = db.Column(db.String(150), default = 'None', unique=False)
    feature7 = db.Column(db.String(150), default = 'None', unique=False)
    feature8 = db.Column(db.String(150), default = 'None', unique=False)
    feature9 = db.Column(db.String(150), default = 'None', unique=False)
    feature10 = db.Column(db.String(150), default = 'None', unique=False)
    feature11 = db.Column(db.String(150), default = 'None', unique=False)
    feature12 = db.Column(db.String(150), default = 'None', unique=False)
    feature13 = db.Column(db.String(150), default = 'None', unique=False)
    feature14 = db.Column(db.String(150), default = 'None', unique=False)
    feature15 = db.Column(db.String(150), default = 'None', unique=False)
    feature16 = db.Column(db.String(150), default = 'None', unique=False)
    feature17 = db.Column(db.String(150), default = 'None', unique=False)
    feature18 = db.Column(db.String(150), default = 'None', unique=False)
    feature19 = db.Column(db.String(150), default = 'None', unique=False)
    feature20 = db.Column(db.String(150), default = 'None', unique=False)
    feature21 = db.Column(db.String(150), default = 'None', unique=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

db.create_all()