from datetime import datetime
from scripts.setup import db
from scripts.guardian import Guardian


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    phone = db.Column(db.String(20), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, username, email, password, phone=None):
        self.username = Guardian.encrypt(username, password)
        self.email = Guardian.encrypt(email, password)
        self.password = Guardian.hash_password(password)
        self.phone = Guardian.encrypt(phone, password)

    def __repr__(self):
        return f'<User {self._decrypt(self.username)}>'

    @classmethod
    def create(cls, username, email, password, phone=None):
        user = cls(username, email, password, phone)
        db.session.add(user)
        db.session.commit()
        return user

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
            self.username = Guardian.encrypt(username, password)
        if email:
            self.email = Guardian.encrypt(email, password)
        if password:
            self.password = Guardian.hash_password(password)
        if phone:
            self.phone = Guardian.encrypt(phone, password)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def authenticate(cls, username: str, password: str):
        try:
            user = User.get_by_username(username)

            if Guardian.verify_password(user.password, password):
                return 12341234

            else:
                return None

        except Exception as e:
            return None
