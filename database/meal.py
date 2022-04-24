import sqlite3
from typing import List
from settings import DATABASE_NAME

class DailyMeal:

    @staticmethod
    def add(data) -> None:
        with sqlite3.connect(DATABASE_NAME) as conn:
            c = conn.cursor()
            # TODO find food_id before inserting
            for d in data:
                c.execute("INSERT INTO food VALUES (?, ?, ?)", d.values())
                conn.commit()

