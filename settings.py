import sqlite3
import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from tables import Base, Food, Meal

DATABASE_NAME = "diet.db"



def create_tables(engine):

    Food.meal = relationship("Meal", order_by = Meal.id, back_populates="food")
    
    Base.metadata.create_all(engine)

def main():
    if not (pathlib.Path(__file__) / DATABASE_NAME).is_file():
        conn = sqlite3.connect(DATABASE_NAME)
        conn.close()

        engine = create_engine("sqlite:///" + DATABASE_NAME, echo=True)

        create_tables(engine)


if __name__ == "__main__":
    main()


    




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
