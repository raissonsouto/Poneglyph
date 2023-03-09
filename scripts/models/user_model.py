from datetime import datetime
from scripts.setup import db, guardian
import sys


def check_password():
    """
    Check if password have minimum size or maximum size
    :return:
    """
    pass


class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.LargeBinary, unique=True, nullable=False)
    email = db.Column(db.LargeBinary, unique=True, nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    phone = db.Column(db.LargeBinary, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username: str, email: str, password: str, phone: str):
        self.username = guardian.encrypt(username)
        self.email = guardian.encrypt(email)
        self.password = guardian.hash_password(password)
        self.phone = guardian.encrypt(phone)
        self.created_at = datetime.now()

        db.session.add(self)
        db.session.commit()

    def __repr__(self) -> str:
        return f'<User {self._decrypt(self.username)}>'

    @classmethod
    def get_by_id(cls, user_id):
        return cls.query.get(user_id)

    @classmethod
    def get_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def update(self, username=None, email=None, password=None, phone=None):
        if username:
            self.username = guardian.encrypt(username, password)
        if email:
            self.email = guardian.encrypt(email, password)
        if password:
            self.password = guardian.hash_password(password)
        if phone:
            self.phone = guardian.encrypt(phone, password)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def authenticate(cls, username: str, password: str):
        try:
            user = User.get_by_username(username)

            if guardian.verify_password(user.password, password):
                return 12341234

            else:
                return None

        except Exception as e:
            return None
