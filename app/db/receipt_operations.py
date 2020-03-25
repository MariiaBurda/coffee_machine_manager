from .config import config_for_db
from .interface_connector import InterfaceConnector


class GetReceiptInfo(InterfaceConnector):
    def get_receipt_info(self, machine_id, receipt_id):
        sql = "SELECT mr.machine_id, r.id, r.name, r.water_ml, r.milk_ml, r. coffee_gr " \
              "FROM machine_receipt AS mr " \
              "INNER JOIN receipt AS r " \
              "ON mr.receipt_id = r.id " \
              f"WHERE mr.machine_id = {self.symbol} AND mr.receipt_id = {self.symbol}"
        data = (machine_id, receipt_id)
        self.cursor.execute(sql, data)
        row = self.cursor.fetchone()

        return row


class GetReceiptsList(InterfaceConnector):
    def get_receipts_list(self):
        sql = "SELECT id, name " \
              "FROM receipt"
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        return rows


def get_receipt_resources_value(machine_id, receipt_id):
    try:
        with GetReceiptInfo(config_for_db) as interface_connector:
            receipt = interface_connector.get_receipt_info(machine_id, receipt_id)
        print(receipt)
        receipt_water_ml = receipt[3]
        receipt_milk_ml = receipt[4]
        receipt_coffee_gr = receipt[5]

        return receipt_water_ml, receipt_milk_ml, receipt_coffee_gr

    except Exception as e:
        print("Something went wrong: {}".format(e))
