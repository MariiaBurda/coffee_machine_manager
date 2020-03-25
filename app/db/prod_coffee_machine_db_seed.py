import sqlite3


def prod_db_seed():
    conn = sqlite3.connect("prod_coffee_machine.db")
    cursor = conn.cursor()

    data_list = [
        ("""
        INSERT INTO machine(id, name, max_water_ml, max_milk_ml, max_coffee_gr, current_water_ml, current_milk_ml, current_coffee_gr)
        VALUES
            (1, 'Lazy coffee', 2000, 500, 1000, 2000, 500, 1000);"""),

        ("""
        INSERT INTO receipt(id, name, water_ml, milk_ml, coffee_gr)
        VALUES
            (1, 'Americano', 50, 0, 20),
            (2, 'Americano with milk', 50, 10, 20),
            (3, 'Latte', 30, 30, 10);"""),
        ("""
        INSERT INTO machine_receipt(machine_id, receipt_id)
        VALUES
            (1, 1), (1, 2), (1, 3);""")]

    for data in data_list:
        cursor.execute(data)

    conn.commit()


if __name__ == "__main__":
    prod_db_seed()
