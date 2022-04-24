from database.food import Food
from database.meal import DailyMeal
import json

if __name__ == "__main__":

    with open("resources/food.json", "r") as f:

        food = json.loads(f.read())

    Food.add(food)

    with open("resources/daily_meal.json", "r") as f:

        daily_meal = json.loads(f.read())

    DailyMeal.add(daily_meal)