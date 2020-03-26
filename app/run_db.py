from app.db.prod_coffee_machine_db_init import prod_db_init
from app.db.prod_coffee_machine_db_seed import prod_db_seed
import os

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, 'prod_coffee_machine.db')


def main(db):
    prod_db_init(db)
    prod_db_seed(db)
    print("Database was created and populated")


if __name__ == "__main__":
    main(db)

