import sqlite3

if __name__ == "__main__":
    #  create databases
    with sqlite3.connect("food.db") as conn:

        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE food (
                name text,
                calories integer,
                base_weight integer
            ) 
            """
        )

        conn.commit()
        c.fetchall()  # what is this for?

    with sqlite3.connect("nutrition.db") as conn:

        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE nutrition (
                date date,
                time time,
                food blob,
                weight blob
            ) 
            """
        )

        conn.commit()
        c.fetchall()  # what is this for?
