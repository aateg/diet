import sqlite3
from food import Food

with sqlite3.connect("food.db") as conn:
    c = conn.cursor()
    c.execute("INSERT INTO food VALUES (:, :, :)".  food.get_data())

    food = Food()

