from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from config import Config

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy()