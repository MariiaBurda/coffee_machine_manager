import mysql.connector
import sys

from .config import config_for_db


def get_receipt_info(machine_id, receipt_id):
    try:
        db = mysql.connector.Connect(**config_for_db)
        cursor = db.cursor()

        sql = "SELECT mr.machine_id, r.id, r.name, r.water_ml, r.milk_ml, r. coffee_gr " \
              "FROM machine_receipt AS mr " \
              "INNER JOIN receipt AS r " \
              "ON mr.receipt_id = r.id " \
              "WHERE mr.machine_id = %s AND mr.receipt_id = %s"
        data = (machine_id, receipt_id)
        cursor.execute(sql, data)
        row = cursor.fetchone()

        return row

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def get_receipts_list():
    try:
        db = mysql.connector.Connect(**config_for_db)
        cursor = db.cursor()

        sql = "SELECT id, name " \
              "FROM receipt"
        cursor.execute(sql,)
        rows = cursor.fetchall()

        return rows

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def get_receipt_resources_value(machine_id, receipt_id):
    try:
        receipt = get_receipt_info(machine_id, receipt_id)
        print(receipt)
        receipt_water_ml = receipt[3]
        receipt_milk_ml = receipt[4]
        receipt_coffee_gr = receipt[5]

        return receipt_water_ml, receipt_milk_ml, receipt_coffee_gr

    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))
