import mysql.connector
import sys

from .config import config_for_db


def fill_resources(machine_id):
    try:
        db = mysql.connector.Connect(**config_for_db)
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


def get_current_value_of_all_resources(machine_id):
    try:
        db = mysql.connector.Connect(**config_for_db)
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


def pull_out_current_value_of_each_resource(machine_id):
    try:
        current_state = get_current_value_of_all_resources(machine_id)
        print(current_state)
        current_water_ml = current_state[2]
        current_milk_ml = current_state[3]
        current_coffee_gr = current_state[4]
        return current_water_ml, current_milk_ml, current_coffee_gr

    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))


def change_current_value_of_used_resources(machine_id, water_ml, milk_ml, coffee_gr):
    try:
        db = mysql.connector.Connect(**config_for_db)
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
