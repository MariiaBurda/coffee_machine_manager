from app.database.initialization.sqlite.sqlite_coffee_machine_db_init import sqlite_db_init
from app.database.initialization.sqlite.sqlite_coffee_machine_db_seed import sqlite_db_seed
import os

path = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(path, 'sqlite_coffee_machine.db')


def main(db):
    sqlite_db_init(db)
    sqlite_db_seed(db)
    print("Database was created and populated")
    print(f"db path: {db}")


if __name__ == "__main__":
    main(db_path)
