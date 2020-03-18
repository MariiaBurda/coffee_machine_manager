import mysql.connector

from .config import config


def get_all_history(machine_id):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "SELECT r.name, h.date FROM history AS h " \
              "INNER JOIN receipt AS r " \
              "ON h.receipt_id = r.id " \
              "WHERE machine_id = %s " \
              "ORDER BY date DESC"
        data = (machine_id,)
        cursor.execute(sql, data)
        rows = cursor.fetchall()

        return rows

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def get_last_orders(machine_id, limit):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "SELECT r.name, h.date FROM history AS h " \
              "INNER JOIN receipt AS r " \
              "ON h.receipt_id = r.id " \
              "WHERE machine_id = %s " \
              "ORDER BY date DESC " \
              "LIMIT %s"

        data = (machine_id, limit)
        cursor.execute(sql, data)
        rows = cursor.fetchall()

        return rows

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()


def add_order_to_history(machine_id, receipt_id):
    try:
        db = mysql.connector.Connect(**config)
        cursor = db.cursor()

        sql = "INSERT INTO history(machine_id, receipt_id, date) " \
              "VALUES(%s, %s, NOW())"
        data = (machine_id, receipt_id)
        cursor.execute(sql, data)

        db.commit()

    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))

    finally:
        cursor.close()
        db.close()

