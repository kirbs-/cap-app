from app import db
import config

import glob
import urllib
from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
import ldap3
import traceback
from datetime import datetime


class User(db.Model):

    ADMINS = [
        'ckirby',
        'divya.aigal',
        'hrushikesh.dhumal',
        'suresh.bhusare'
    ]

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(1000))
    password = db.Column(db.Binary(60))
    login_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, login, password):
        self.login = login
        # self.password = password

    @staticmethod
    def try_login(username, password, domain='new_sterling'):
        try:
            conn = ldap3.Connection(config.LDAP_PROVIDER_URL, user='{}\\{}'.format(domain, username), password=password, authentication=ldap3.NTLM, auto_bind=True)
        except:
            traceback.print_exc()

    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.login

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return True

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    @property
    def admin(self):
        return self.login in User.ADMINS

    # @password.setter
    # def set_password(self, plaintext_password):
    #     self.password = bcrypt.generate_password_hash(plaintext_password)

    @hybrid_method
    def is_correct_password(self, plaintext_password):
        return bcrypt.check_password_hash(self.password, plaintext_password)

