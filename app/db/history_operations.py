from .interface_connector import InterfaceConnector


class GetLastOrders(InterfaceConnector):
    def get_last_orders(self, machine_id, limit):
        sql = "SELECT r.name, h.date " \
              "FROM history AS h " \
              "INNER JOIN receipt AS r " \
              "ON h.receipt_id = r.id " \
              f"WHERE machine_id = {self.symbol} " \
              "ORDER BY date DESC " \
              f"LIMIT {self.symbol}"
        data = (machine_id, limit)
        self.cursor.execute(sql, data)

        rows = self.cursor.fetchall()
        print(f'rows: {rows}')

        mapped_rows = ''
        if self.db_sys == 'mysql':
            mapped_rows = mapper_for_mysql(rows)
        elif self.db_sys == 'sqlite':
            mapped_rows = rows

        return mapped_rows


class AddOrderToHistory(InterfaceConnector):
    def add_order_to_history(self, machine_id, receipt_id):
        sql = "INSERT INTO history(machine_id, receipt_id, date) " \
              f"VALUES({self.symbol}, {self.symbol}, {self.time})"
        data = (machine_id, receipt_id)
        self.cursor.execute(sql, data)

        self.db.commit()


class GetStatisticOfUsedResources(InterfaceConnector):
    def get_statistic_of_used_resources(self, machine_id):
        sql = "SELECT r.name, COUNT(h.id) AS number_of_orders " \
              "FROM receipt AS r " \
              "INNER JOIN history AS h " \
              "ON r.id = h.receipt_id " \
              f"WHERE h.machine_id = {self.symbol} " \
              "GROUP BY h.receipt_id "
        data = (machine_id,)
        self.cursor.execute(sql, data)
        rows = self.cursor.fetchall()

        return rows


def mapper_for_mysql(last_orders):
    mapped_orders = list(map(lambda x: (x[0], x[1].strftime("%d-%m-%Y, %H:%M:%S")), last_orders))
    return mapped_orders
