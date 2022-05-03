from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()

class Food(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    energy = Column(Integer)
    base_weight = Column(Integer)
    unit = Column(String)
    fat = Column(Float)
    carbohydrates = Column(Float)
    sugar = Column(Float)
    protein = Column(Float)

class Meal(Base):
    __tablename__ = 'meal'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    time = Column(Time)
    food_id = Column(Integer, ForeignKey('food.id'))
    weight = Column(Integer)
    food = relationship("Food", back_populates='meal')