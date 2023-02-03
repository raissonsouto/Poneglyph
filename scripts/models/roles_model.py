from datetime import datetime
from scripts.setup import db
from scripts.guardian import Guardian


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __repr__(self):
        return f'<Role {self.name}>'

    @classmethod
    def create(cls, name, capacity):
        role = cls(name, capacity)
        db.session.add(role)
        db.session.commit()
        return role

    @classmethod
    def get(cls, role_id):
        return cls.query.get(role_id)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def update(self, name, capacity):
        self.name = name
        self.capacity = capacity
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
