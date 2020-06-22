from flask_migrate import Migrate
from application import app
from application.model import db

#database management
migrate = Migrate(app, db)