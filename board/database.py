from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True, nullable=True)
    title = db.Column(db.String(50), nullable=True)
    artist = db.Column(db.String(50), nullable=True)
    folder = db.Column(db.String(20))
    created = db.Column(db.DateTime, default=datetime.now)