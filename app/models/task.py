from app.backend.db import Base
from sqlalchemy import INTEGER, String, ForeignKey, Column, BOOLEAN
from sqlalchemy.orm import relationship
from app.models import *


class Task(Base):
    __tablename__ = 'tasks'
    __table_args__ = {'keep_existing': True}
    id = Column(INTEGER, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(INTEGER, default=0)
    completed = Column(BOOLEAN, default=False)
    user_id = Column(INTEGER, ForeignKey('users.id'), nullable=False, index=True)
    slug = Column(String, unique=True)


user = relationship('User', back_populates='task')

from sqlalchemy.schema import CreateTable

print(CreateTable(Task.__table__))
