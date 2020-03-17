import mysql.connector

from config import config


def get_all_history(machine_id):
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


def get_last_orders(machine_id, limit):
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

