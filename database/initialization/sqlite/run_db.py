from database.initialization.sqlite.sqlite_coffee_machine_db_init import sqlite_db_init
from database.initialization.sqlite.sqlite_coffee_machine_db_seed import sqlite_db_seed
import os

path = os.path.dirname(os.path.abspath(__file__))
db = os.path.join(path, 'sqlite_coffee_machine.db')


def main(db_path):
    sqlite_db_init(db_path)
    sqlite_db_seed(db_path)
    print("Database was created and populated")
    print(f"db path: {db_path}")


if __name__ == "__main__":
    main(db)

