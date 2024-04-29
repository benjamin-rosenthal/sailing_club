import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from database import db

app = Flask(__name__)

# JWT setup
load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Views
from auth import views

# Database migrations
from config import Config
app.config.from_object(Config) 
db.init_app(app)
from auth.models.user import User
from membership.models.membership import Membership
from membership.models.membership_status import MembershipStatus
migrate = Migrate(app, db)