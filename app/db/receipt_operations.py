import mysql.connector

from .config import config


def get_receipt_info(machine_id, receipt_id):
    try:
        db = mysql.connector.Connect(**config)
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
        db = mysql.connector.Connect(**config)
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

