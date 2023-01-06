import sqlite3

DATABASE_NAME = "nutrition.db"

if __name__ == "__main__":
    with sqlite3.connect(DATABASE_NAME) as conn:

        c = conn.cursor()
        c.execute(
            """
            CREATE TABLE food (
                food_id integer PRIMARY KEY,
                name text NOT NULL,
                energy integer NOT NULL,
                base_weight integer,
                unit text,
                fat real,
                carbohydrates real,
                sugar real,
                protein real
            ); 
            
            CREATE TABLE meals (
                meal_id integer PRIMARY KEY,
                date date,
                time text,
                food_id integer,
                weight integer,
                FOREIGN KEY (food_id)
                    REFERENCES food (food_id)
            ); 
            """
        )

        conn.commit()
        c.fetchall()  # what is this for?
