from flask import Blueprint, render_template, flash, redirect, url_for, session
from application.auth.auth import  is_logged_in

dashboard_bp = Blueprint(__name__, 'dashboard_bd')
is_logged_in = is_logged_in


@dashboard_bp.route('/')
@is_logged_in
def dashboard():
    return render_template('admin/dashboard.html')

