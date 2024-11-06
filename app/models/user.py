from app.backend.db import Base
from sqlalchemy import INTEGER, String, ForeignKey, Column, BOOLEAN
from sqlalchemy.orm import relationship
from app.models import *


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(INTEGER, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(INTEGER)
    slug = Column(String, unique=True, index=True)


task = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable

print(CreateTable(User.__table__))

