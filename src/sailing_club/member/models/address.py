from sqlalchemy.orm import declarative_base
from sailing_club.database import db

Base = declarative_base()

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address_1 = db.Column(db.String())
    address_2 = db.Column(db.String(), nullable=False)
    city = db.Column(db.String())
    state = db.Column(db.String())
    zip = db.Column(db.Integer)