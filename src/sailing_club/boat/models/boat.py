from sqlalchemy.orm import declarative_base
from sailing_club.app import db

Base = declarative_base()

class Boat(db.Model):
    __tablename__ = 'boat'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marina_id = db.Column(db.Integer, nullable=False)
    boat_name = db.Column(db.String(), nullable=False)
    manufacturer = db.Column(db.String(), nullable=False)
    model = db.Column(db.String(), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    draft_feet = db.Column(db.Integer, nullable=False)
    draft_inches = db.Column(db.Integer, nullable=False)
    color_hull = db.Column(db.String(), nullable=False)
    color_canvas = db.Column(db.String(), nullable=False)
    sail_number = db.Column(db.Integer, nullable=False)