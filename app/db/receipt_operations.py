import mysql.connector

from config import config


def get_receipt_info(machine_id, receipt_id):
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