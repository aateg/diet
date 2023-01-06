from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship

# connect to database
engine = create_engine('sqlite:///diet.db', echo=True)
# manage tables
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

    def __init__(self, name, energy, base_weight, unit, fat, carbohydrates, sugar, protein):
        self.name = name
        self.energy = energy
        self.base_weight = base_weight
        self.unit = unit
        self.fat = fat
        self.carbohydrates = carbohydrates
        self.sugar = sugar
        self.protein = protein

# class Meal(Base):
#     __tablename__ = 'meal'

#     meal_id = Column(Integer, primary_key=True)
#     date = Column(Date)
#     time = Column(Time)
#     food_id = Column(Integer, ForeignKey('food.id'))
#     weight = Column(Integer)
#     food = relationship("Food", back_populates='meal')

#     def __init__(self, date, time, food_id, weight):
#         self.date = date
#         self.time = time
#         self.food_id = food_id
#         self.weight = weight

Base.metadata.create_all(engine)