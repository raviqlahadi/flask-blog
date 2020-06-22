from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'table_users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.now())
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.username