from sqlalchemy import Column, Integer, String
from .database import Base

class CV(Base):
    __tablename__ = "cvs"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)