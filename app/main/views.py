from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app
from . import bp


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
