from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from . import bp

from ..models import User
from .. import db


@bp.route('/', methods=['GET', 'POST'])
def index():
    user = User()
    user.username = "thunderstr"
    user.email = "sina@gmail.com"
    user.password = "sdlfkjasdlfkjldkfj"
    db.session.add(user)
    db.session.commit()

    us = User.query.filter_by(id=1).first()
    return us

