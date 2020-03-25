import sqlite3

machine_id = 1
receipt_id = 2


def get_all_receipts():
    conn = sqlite3.connect("prod_coffee_machine.db")
    cursor = conn.cursor()

    sql = "SELECT id, name " \
          "FROM receipt"
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows


def get_receipt_resources_value(machine_id, receipt_id):
    conn = sqlite3.connect("prod_coffee_machine.db")
    cursor = conn.cursor()

    sql = "SELECT mr.machine_id, r.id, r.name, r.water_ml, r.milk_ml, r. coffee_gr " \
          "FROM machine_receipt AS mr " \
          "INNER JOIN receipt AS r " \
          "ON mr.receipt_id = r.id " \
          "WHERE mr.machine_id=? AND mr.receipt_id=?"
    data = (machine_id, receipt_id)
    cursor.execute(sql, data)
    row = cursor.fetchone()

    return row


if __name__ == '__main__':
    receipts_list = get_all_receipts()
    print(receipts_list)

    receipt_resources_value_list = get_receipt_resources_value(machine_id, receipt_id)
    print(receipt_resources_value_list)
