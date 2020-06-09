from flask import Blueprint, render_template

posts_bp = Blueprint(__name__, 'posts_bd')

@posts_bp.route('/')
def posts():
    return render_template('admin/posts.html')
