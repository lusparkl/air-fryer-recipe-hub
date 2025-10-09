from sqlalchemy import Integer, String, Column, JSON
from base import Base

class Recipe(Base):
    __tablename__="recipes"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255), nullable=False)
    prep_time = Column(Integer, nullable=False)
    overall_time = Column(Integer, nullable=False)
    calories = Column(Integer, nullable=False)
    fat = Column(Integer, nullable=False)
    carbs = Column(Integer, nullable=False)
    protein = Column(Integer, nullable=False)
    ingridients = Column(JSON, nullable=False)
    directions = Column(JSON, nullable=False)
    image = Column(String(255), nullable=True)
    categories = Column(JSON, nullable=False)