from app.db.prod_coffee_machine_db_init import prod_db_init
from app.db.prod_coffee_machine_db_seed import prod_db_seed


def main():
    prod_db_init()
    prod_db_seed()
    print("Test database was created and populated")


if __name__ == "__main__":
    main()
