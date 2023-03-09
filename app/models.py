from sqlalchemy import Integer, String, Boolean
from sqlalchemy.sql.schema import Column

from app.database import Model

class Creation(Model):
    __tablename__ = 'creations'

    id = Column(Integer, primary_key=True)
    type = Column(String(30), nullable=True)
    description = Column(String(250), nullable=True)
    image = Column(String, nullable=True)   
    link = Column(String(500), nullable=True)
    is_published = Column(Boolean, default=True)
