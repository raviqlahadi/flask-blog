from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from .model import db, User


def crete_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    db.init_app(app)

    #import blueprint
    from application.auth.auth import auth_bp
    from application.dashboard.dashboard import dashboard_bp
    from application.users.users import users_bp
    from application.posts.posts import posts_bp

    #register blueprint
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
    app.register_blueprint(posts_bp, url_prefix='/posts')
    app.register_blueprint(users_bp, url_prefix='/users')

    return app


app = crete_app()

@app.route('/')
def home():
   
    return render_template('index.html')
