from datetime import datetime

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uid = db.mapped_column(db.Integer, primary_key=True)
    username = db.mapped_column(db.String(50), unique=True, nullable=False)
    password = db.mapped_column(db.String(30))
    created_at = db.mapped_column(db.DateTime, default=datetime.utcnow)

    def __str__(self):
        return self.username
    
class Story(db.Model):
    stid = db.mapped_column(db.Integer, primary_key=True)
    sttitle = db.mapped_column(db.String(50), unique=True)
    stbody = db.mapped_column(db.Text, nullable=False)
    created_at = db.mapped_column(db.DateTime, default=datetime.utcnow)
    story_teller_id = db.mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    story_teller = db.relationship('User', backref=db.backref('story', lazy=True))

    def __str__(self):
        return f'"{self.sttitle}" by {self.story_teller} ({self.created_at:%Y-%m-%d})'
