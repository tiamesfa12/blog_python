from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True) #email has a max length of 150
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), unique=True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) #func will it by default if there is no other information
    posts = db.relationship('Post', backref='user', passive_deletes=True) #backref means back reference, which allows you to write and access the user data
    comments = db.relationship('Comment', backref='user', passive_deletes=True)
    likes = db.relationship('Like', backref='user', passive_deletes=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False) # when i delete the user, delete all the posts the user has
    comments = db.relationship('Comment', backref='post', passive_deletes=True)
    likes = db.relationship('Like', backref='post', passive_deletes=True)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now()) 
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete="CASCADE"), nullable=False)
    