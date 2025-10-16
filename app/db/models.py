from sqlalchemy import Integer, String, Column, JSON, Text
from app.db.base import Base

class Recipe(Base):
    __tablename__="recipes"
    
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    prep_time = Column(Integer, nullable=False)
    overall_time = Column(Integer, nullable=False)
    calories = Column(Integer, nullable=False)
    fat = Column(Integer, nullable=False)
    carbs = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    ingridients = Column(JSON, nullable=False)
    directions = Column(JSON, nullable=False)
    image = Column(Text, nullable=True)
    categories = Column(JSON, nullable=True)