from .interface_connector import InterfaceConnector


class GetLastOrders(InterfaceConnector):
    def get_last_orders(self, machine_id, limit):
        sql = "SELECT r.name, h.date FROM history AS h " \
              "INNER JOIN receipt AS r " \
              "ON h.receipt_id = r.id " \
              "WHERE machine_id = %s " \
              "ORDER BY date DESC " \
              "LIMIT %s"
        data = (machine_id, limit)
        self.cursor.execute(sql, data)
        rows = self.cursor.fetchall()

        return rows


class AddOrderToHistory(InterfaceConnector):
    def add_order_to_history(self, machine_id, receipt_id):
        sql = "INSERT INTO history(machine_id, receipt_id, date) " \
              "VALUES(%s, %s, NOW())"
        data = (machine_id, receipt_id)
        self.cursor.execute(sql, data)

        self.db.commit()


class GetStatisticOfUsedResources(InterfaceConnector):
    def get_statistic_of_used_resources(self, machine_id):
        sql = "SELECT r.name, COUNT(h.id) AS number_of_orders " \
              "FROM receipt AS r " \
              "INNER JOIN history AS h " \
              "ON r.id = h.receipt_id " \
              "WHERE h.machine_id = %s " \
              "GROUP BY h.receipt_id "
        data = (machine_id,)
        self.cursor.execute(sql, data)
        rows = self.cursor.fetchall()

        return rows
