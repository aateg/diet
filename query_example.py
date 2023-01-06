# how to query the database
from sqlalchemy.orm import sessionmaker
from create_tables import Food, engine

Session = sessionmaker(bind = engine)
session = Session()

# query the database
# query all foods
foods = session.query(Food).all()
# print the foods
for food in foods:
    print(food.name, food.energy, food.base_weight, food.unit, food.fat, food.carbohydrates, food.sugar, food.protein)

# query a specific food
food = session.query(Food).filter_by(name = 'apple').first()
print(food.name, food.energy, food.base_weight, food.unit, food.fat, food.carbohydrates, food.sugar, food.protein)

