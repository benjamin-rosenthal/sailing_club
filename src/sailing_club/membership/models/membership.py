from sqlalchemy import ForeignKeyConstraint
from sqlalchemy.orm import declarative_base
from sailing_club.database import db
from sailing_club.membership.models.membership_status import MembershipStatus

Base = declarative_base()

class Membership(db.Model):
    __tablename__ = 'membership'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_id = db.Column(db.Integer, nullable=False)

    __table_args__ = (        
            ForeignKeyConstraint([status_id], [MembershipStatus.id], ondelete='NO ACTION'),        
    )