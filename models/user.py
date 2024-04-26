from typing import Optional

from sqlalchemy import Column, PrimaryKeyConstraint, String
from sqlalchemy.orm import mapped_column
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    __table_args__ = (
        PrimaryKeyConstraint('email', name='email_pkey'),
    )

    email: str = Field(sa_column=mapped_column('email', String(256)))
    password: Optional[str] = Field(default=None, sa_column=mapped_column('password', String(256)))