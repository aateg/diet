from sqlalchemy.orm import sessionmaker
from create_tables import Food, engine

Session = sessionmaker(bind = engine)
session = Session()

# create a list of foods
foods = [
    Food(name = 'apple', energy = 52, base_weight = 100, unit = 'g', fat = 0.3, carbohydrates = 13.8, sugar = 10.4, protein = 0.3),
    Food(name = 'banana', energy = 89, base_weight = 100, unit = 'g', fat = 0.3, carbohydrates = 22.8, sugar = 12.7, protein = 1.1),
    Food(name = 'orange', energy = 47, base_weight = 100, unit = 'g', fat = 0.1, carbohydrates = 11.8, sugar = 8.7, protein = 0.9),
    Food(name = 'pear', energy = 57, base_weight = 100, unit = 'g', fat = 0.2, carbohydrates = 14.7, sugar = 10.5, protein = 0.4),
    Food(name = 'pineapple', energy = 50, base_weight = 100, unit = 'g', fat = 0.2, carbohydrates = 12.6, sugar = 9.9, protein = 0.5),
    Food(name = 'strawberry', energy = 32, base_weight = 100, unit = 'g', fat = 0.3, carbohydrates = 7.7, sugar = 5.6, protein = 0.7),
    Food(name = 'watermelon', energy = 30, base_weight = 100, unit = 'g', fat = 0.2, carbohydrates = 7.6, sugar = 6.1, protein = 0.6)
]

# add the foods to the session
session.add_all(foods)
# commit the session
session.commit()
