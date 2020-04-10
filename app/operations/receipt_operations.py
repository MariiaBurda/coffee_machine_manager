from .interface_connector import Closing
from .base_operation import BaseOperation


class ReceiptOperations(BaseOperation):
    def get_receipt_info(self, machine_id, receipt_id):
        with Closing(self.connector) as closing:
            sql = "SELECT mr.machine_id, r.id, r.name, r.water_ml, r.milk_ml, r. coffee_gr " \
                  "FROM machine_receipt AS mr " \
                  "INNER JOIN receipt AS r " \
                  "ON mr.receipt_id = r.id " \
                  f"WHERE mr.machine_id = {closing.symbol} AND mr.receipt_id = {closing.symbol}"
            data = (machine_id, receipt_id)
            closing.cursor.execute(sql, data)
            row = closing.cursor.fetchone()

            return row

    def get_receipts_list(self):
        with Closing(self.connector) as closing:
            sql = "SELECT id, name " \
                  "FROM receipt"
            closing.cursor.execute(sql)
            rows = closing.cursor.fetchall()
            return rows

    def get_receipt_resources_value(self, machine_id, receipt_id):
        try:
            receipt = self.get_receipt_info(machine_id, receipt_id)
            print(receipt)
            receipt_water_ml = receipt[3]
            receipt_milk_ml = receipt[4]
            receipt_coffee_gr = receipt[5]

            return receipt_water_ml, receipt_milk_ml, receipt_coffee_gr

        except Exception as e:
            print("Something went wrong: {}".format(e))
