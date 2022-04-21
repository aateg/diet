from typing import List


class Meal:
    def __init__(self) -> "Meal":
        self.date


class DailyMeal:
    def __init__(self) -> "DailyMeal":
        self.meals: List[Meal] = []

    def add_meal(self, meal: Meal) -> None:
        self.meals.append(meal)

