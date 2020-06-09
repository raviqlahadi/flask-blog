from flask import Blueprint, render_template

dashboard_bp = Blueprint(__name__, 'dashboard_bd')

@dashboard_bp.route('/')
def dashboard():
    return render_template('admin/dashboard.html')
