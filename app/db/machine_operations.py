import mysql.connector

from config import config


def fill_resources(machine_id):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "UPDATE machine " \
              "SET current_water_ml = max_water_ml, " \
              "current_milk_ml = max_milk_ml, " \
              "current_coffee_gr = max_coffee_gr " \
              "WHERE id = %s"
        data = (machine_id,)
        cursor.execute(sql, data)

        db.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def get_current_state(machine_id):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "SELECT id, name, current_water_ml, current_milk_ml, current_coffee_gr " \
              "FROM machine " \
              "WHERE id = %s"
        data = (machine_id,)
        cursor.execute(sql, data)
        row = cursor.fetchone()

        return row

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def change_current_state(machine_id, water_ml, milk_ml, coffee_gr):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "UPDATE machine " \
              "SET current_water_ml = current_water_ml - %s, " \
              "current_milk_ml = current_milk_ml - %s, " \
              "current_coffee_gr = current_coffee_gr - %s " \
              "WHERE id = %s"
        data = (water_ml, milk_ml, coffee_gr, machine_id)
        cursor.execute(sql, data)

        db.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()
