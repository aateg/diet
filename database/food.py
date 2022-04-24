import sqlite3
from typing import Any, Dict, Tuple, List
from settings import DATABASE_NAME


class Food:

    @staticmethod
    def add(data: List[Dict[Any, Any]]) -> None:
        
        with sqlite3.connect(DATABASE_NAME) as conn:
            c = conn.cursor()
            for d in data:
                c.execute("INSERT INTO food VALUES (?, ?, ?)", d.values())
                conn.commit()

