from sqlalchemy.orm import declarative_base
from sailing_club.database import db

Base = declarative_base()

class Member(db.Model):
    __tablename__ = 'member'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    membership_id = db.Column(db.Integer)
    boat_id = db.Column(db.Integer)
    address_id = db.Column(db.Integer)
    name_first = db.Column(db.String(), nullable=False)
    name_last = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    number_mobile = db.Column(db.String(), nullable=False)
    number_landline = db.Column(db.String())
    number_office = db.Column(db.String())