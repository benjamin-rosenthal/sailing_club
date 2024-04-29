import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from database import db

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Views
from auth import views

# Database related part
from config import Config
app.config.from_object(Config) 
db.init_app(app)
from auth.models.user import User
migrate = Migrate(app, db)