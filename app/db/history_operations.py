from .interface_connector import Closing
from .base_operation import BaseOperation


class HistoryOperations(BaseOperation):
    def get_last_orders(self, machine_id, limit):
        with Closing(self.connector) as closing:
            sql = "SELECT r.name, h.date " \
                  "FROM history AS h " \
                  "INNER JOIN receipt AS r " \
                  "ON h.receipt_id = r.id " \
                  f"WHERE machine_id = {closing.symbol} " \
                  "ORDER BY date DESC " \
                  f"LIMIT {closing.symbol}"
            data = (machine_id, limit)
            closing.cursor.execute(sql, data)

            rows = closing.cursor.fetchall()
            print(f'rows: {rows}')

            mapped_rows = self.mapper.map_orders(rows)
            return mapped_rows

    def add_order_to_history(self, machine_id, receipt_id):
        with Closing(self.connector) as closing:
            sql = "INSERT INTO history(machine_id, receipt_id, date) " \
                  f"VALUES({closing.symbol}, {closing.symbol}, {closing.time})"
            data = (machine_id, receipt_id)
            closing.cursor.execute(sql, data)

            closing.db.commit()

    def get_statistic_of_used_resources(self, machine_id):
        with Closing(self.connector) as closing:
            sql = "SELECT r.name, COUNT(h.id) AS number_of_orders " \
                  "FROM receipt AS r " \
                  "INNER JOIN history AS h " \
                  "ON r.id = h.receipt_id " \
                  f"WHERE h.machine_id = {closing.symbol} " \
                  "GROUP BY h.receipt_id "
            data = (machine_id,)
            closing.cursor.execute(sql, data)
            rows = closing.cursor.fetchall()

            return rows
