import sqlite3


def sqlite_db_init(db):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    tables = [
        (
            """
            CREATE TABLE receipt(
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(20),
                water_ml INT,
                milk_ml INT,
                coffee_gr INT
            );
            """
        ),
        (
            """
            CREATE TABLE machine(
                id INTEGER NOT NULL PRIMARY KEY,
                name VARCHAR(20),
                max_water_ml INT, 
                max_milk_ml INT,
                max_coffee_gr INT,
                current_water_ml INT, 
                current_milk_ml INT,
                current_coffee_gr INT
            );
            """
        ),
        (
            """
            CREATE TABLE machine_receipt(
                machine_id INTEGER NOT NULL,
                receipt_id INTEGER NOT NULL,
                PRIMARY KEY(machine_id,receipt_id),
                   FOREIGN KEY(machine_id) 
                       REFERENCES machine(id),
                   FOREIGN KEY(receipt_id) 
                       REFERENCES receipt(id)
            );
            """
        ),
        (
            """
            CREATE TABLE history(
                id INTEGER NOT NULL PRIMARY KEY,
                machine_id INTEGER,
                receipt_id INTEGER,
                date DATETIME,
                   FOREIGN KEY(machine_id) 
                       REFERENCES machine(id),
                   FOREIGN KEY(receipt_id) 
                       REFERENCES receipt(id)
            );
            """
        )
    ]

    for table in tables:
        cursor.execute(table)


if __name__ == "__main__":
    sqlite_db_init()
