import os
from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__, template_folder='templates')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

# JWT setup
load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Views
from sailing_club import auth
from sailing_club.auth import views
from . import auth

app.register_blueprint(auth.bp)

# Database migrations
from sailing_club.config import Config
app.config.from_object(Config) 
from sailing_club.auth.models.user import User
from sailing_club.boat.models.boat import Boat
from sailing_club.boat.models.marina import Marina
from sailing_club.membership.models.membership import Membership
from sailing_club.membership.models.membership_status import MembershipStatus
migrate = Migrate(app, db)