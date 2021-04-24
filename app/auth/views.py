from flask import render_template, redirect, url_for, abort, flash, request,\
    current_app

from . import bp


@bp.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('auth/register.html')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('auth/register.html')


@bp.route('/logout')
def logout():
    return "LOGOUT"

