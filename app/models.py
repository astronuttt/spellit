from . import db
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    confirmed = db.Column(db.Boolean, default=False)
    name = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))
    words = db.relationship('Word', backref='creator', lazy='dynamic')
    games = db.relationship('Game', backref='player', lazy='dynamic')


class Word(db.Model):
    __tablename__ = 'words'

    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64))
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'))


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    game_type = db.Column(db.Integer, default=1, nullable=False)
    player_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    words = db.relationship('Word')
