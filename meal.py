from sqlalchemy.orm import sessionmaker
from create_tables import Food, engine

class Meal():
    def __init__(self, meal):
        self.meal = meal

    @classmethod
    def from_json(cls, json: str):
        meal = []
        for food in json:
            meal.update({food['name']: food['weight']})
        return cls(meal)

    def summary(self):

        meal = self._query_foods(self.meal)
        for food in meal:
            print(food.name, food.energy, food.base_weight, food.unit, food.fat, food.carbohydrates, food.sugar, food.protein)

    def _query_foods(self, foods):
        Session = sessionmaker(bind = engine)
        session = Session()

        meal = session.query(Food).filter(Food.name.in_([food["name"] for food in self.meal])).all()

        return meal


meal = Meal([{"name": "apple", "weight":100}, {"name": "banana", "weight": 100}])
meal.summary()

