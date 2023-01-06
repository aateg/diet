class CuttingDiet:

    def __init__(self, body_weight):

        self.body_weight = body_weight
        self.ideal_protein = 2 * body_weight # 2g/kg
        self.ideal_carbohydrates = 2 * body_weight # 2g/kg
        self.ideal_fat = 1 * body_weight # 1g/kg

    def evaluate_meal(self, daily_meal):
        """Evaluates a daily meal against the diet.
        """

        info = daily_meal.summary()

        # Calculate the difference between the ideal and the actual values
        diff = {}
        diff["total_energy"] = info["energy"]
        diff["protein"] = (info["protein"] - self.ideal_protein) > 0
        diff["carbohydrates"] = (info["carbohydrates"] - self.ideal_carbohydrates) <= 0
        diff["fat"] = (info["fat"] - self.ideal_fat) <= 0

        return diff

class BulkingDiet:

    def __init__(self, body_weight):

        self.body_weight = body_weight
        self.ideal_protein = 2 * body_weight # 2g/kg
        self.ideal_carbohydrates = 4 * body_weight # 2g/kg
        self.ideal_fat = 1 * body_weight # 1g/kg

    def evaluate_meal(self, daily_meal):
        """Evaluates a daily meal against the diet.
        """

        info = daily_meal.summary()

        # Calculate the difference between the ideal and the actual values
        diff = {}
        diff["total_energy"] = info["energy"]
        diff["protein"] = (info["protein"] - self.ideal_protein) > 0
        diff["carbohydrates"] = (info["carbohydrates"] - self.ideal_carbohydrates) >= 0
        diff["fat"] = (info["fat"] - self.ideal_fat) <= 0

        return diff