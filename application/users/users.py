from flask import Blueprint, render_template

users_bp = Blueprint(__name__, 'users_bd')

@users_bp.route('/')
def users():
    return render_template('admin/users.html')
