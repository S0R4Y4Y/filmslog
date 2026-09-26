from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(200))
    genre = db.Column(db.String(100))
    rating = db.Column(db.Integer)
    review_text = db.Column(db.String(10000))
    poster_image = db.Column(db.String(500))
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    background_image = db.Column(db.String(500))
    diary_title = db.Column(db.String(200))
    reviews = db.relationship('Review')