from sqlalchemy.orm import sessionmaker
from create_tables import Food, engine

meal = {"apple": 200, "banana": 311} # grams

class Meal:
    def __init__(self, meal):
        self.meal = meal
        self.info = self.summary()

    @classmethod
    def from_json(cls, json: str):
        meal = {}
        for food in json:
            meal.update({food['name']: food['weight']})
        return cls(meal)

    def summary(self):
        info = {}

        for food in self._query_foods():

            f = self.meal[food.name] / food.base_weight
            info["energy"] = info.get("energy", 0) + f * food.energy
            info["protein"] = info.get("protein", 0) + f * food.protein
            info["carbohydrates"] = info.get("carbohydrates", 0) + f * food.carbohydrates
            info["sugar"] = info.get("sugar", 0) + f * food.sugar
            info["fat"] = info.get("fat", 0) + f * food.fat

        return info

    def _query_foods(self):
        Session = sessionmaker(bind = engine)
        session = Session()

        return session.query(Food).filter(Food.name.in_([key for key in self.meal.keys()])).all()

class DailyMeal:
    def __init__(self, meals):
        self.meals = meals

    @classmethod
    def from_json(cls, json: str):
        meals = []
        for meal in json:
            meals.append(Meal.from_json(meal))
        return cls(meals)

    def summary(self):
        info = {}
        for meal in self.meals:
            for key in meal.info.keys():
                info[key] = info.get(key, 0) + meal.info[key]
        return info

meal = Meal(meal)
print(meal.summary())
