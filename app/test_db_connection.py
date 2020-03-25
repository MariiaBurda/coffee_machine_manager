import sqlite3

conn = sqlite3.connect("prod_coffee_machine.db")
cursor = conn.cursor()

machine_id = 1
receipt_id = 2

sql = "SELECT id, name " \
      "FROM receipt"
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)


sql = "SELECT mr.machine_id, r.id, r.name, r.water_ml, r.milk_ml, r. coffee_gr " \
      "FROM machine_receipt AS mr " \
      "INNER JOIN receipt AS r " \
      "ON mr.receipt_id = r.id " \
      "WHERE mr.machine_id=? AND mr.receipt_id=?"
data = (machine_id, receipt_id)
cursor.execute(sql, data)
row = cursor.fetchone()

print(row)
