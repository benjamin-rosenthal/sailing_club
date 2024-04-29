from sqlalchemy.orm import declarative_base
from database import db

Base = declarative_base()

class MembershipStatus(db.Model):
    __tablename__ = 'membership_status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripton = db.Column(db.String(), unique=True, nullable=False)