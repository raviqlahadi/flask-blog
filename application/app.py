from flask import Flask, render_template
#from example_bp import example_bp
from application.auth.auth import auth_bp
from application.dashboard.dashboard import dashboard_bp
from application.users.users import users_bp
from application.posts.posts import posts_bp

app = Flask(__name__)
#app.register_blueprint(example_bp, url_prefix='/bp')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
app.register_blueprint(posts_bp, url_prefix='/posts')
app.register_blueprint(users_bp, url_prefix='/users')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)