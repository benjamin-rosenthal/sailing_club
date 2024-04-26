from flask import Flask
from flask_jwt_extended import JWTManager

from dotenv import load_dotenv
import os

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
load_dotenv()
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
jwt = JWTManager(app)

# Views
from auth import views