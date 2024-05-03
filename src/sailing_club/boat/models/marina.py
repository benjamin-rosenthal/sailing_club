from sqlalchemy.orm import declarative_base
from sailing_club.database import db

Base = declarative_base()

class Marina(db.Model):
    __tablename__ = 'marina'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marina_name = db.Column(db.String(), nullable=False)
    waterway = db.Column(db.String(), nullable=False)
    tributary_of = db.Column(db.String(), nullable=False)