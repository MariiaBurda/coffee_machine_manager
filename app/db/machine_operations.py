import mysql.connector

from config import config


def fill_resources(machine_id):
    db = mysql.connector.Connect(**config)
    cursor = db.cursor()

    sql = "UPDATE machine " \
          "SET current_water_ml = max_water_ml, current_milk_ml = max_milk_ml, current_coffee_gr = max_coffee_gr " \
          "WHERE id = %s"
    data = (machine_id,)
    cursor.execute(sql, data)

    db.commit()

