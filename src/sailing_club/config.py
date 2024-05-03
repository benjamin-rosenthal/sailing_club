from dotenv import load_dotenv
import os
class Config:
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.getenv("CONNECTION_STRING")
    SQLALCHEMY_TRACK_MODIFICATIONS = False