from flask import Blueprint, render_template

auth_bp = Blueprint(__name__, 'auth_bp')

@auth_bp.route('/')
@auth_bp.route('/login')
def login():
   return render_template('admin/login.html')

