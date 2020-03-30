from .config import config_for_db
from .interface_connector import InterfaceConnector


class MachineOperations(InterfaceConnector):
    def fill_resources(self, machine_id):
        sql = "UPDATE machine " \
              "SET current_water_ml = max_water_ml, " \
              "current_milk_ml = max_milk_ml, " \
              "current_coffee_gr = max_coffee_gr " \
              f"WHERE id = {self.symbol}"
        data = (machine_id,)
        self.cursor.execute(sql, data)

        self.db.commit()

    def get_current_value_of_all_resources(self, machine_id):
        sql = "SELECT id, name, current_water_ml, current_milk_ml, current_coffee_gr " \
              "FROM machine " \
              f"WHERE id = {self.symbol}"
        data = (machine_id,)
        self.cursor.execute(sql, data)
        row = self.cursor.fetchone()

        return row

    def change_current_value_of_used_resources(self, machine_id, water_ml, milk_ml, coffee_gr):
        sql = "UPDATE machine " \
                   f"SET current_water_ml = current_water_ml - {self.symbol}, " \
                   f"current_milk_ml = current_milk_ml - {self.symbol}, " \
                   f"current_coffee_gr = current_coffee_gr - {self.symbol} " \
                   f"WHERE id = {self.symbol}"
        data = (water_ml, milk_ml, coffee_gr, machine_id)
        self.cursor.execute(sql, data)

        self.db.commit()

    @staticmethod
    def pull_out_current_value_of_each_resource(machine_id):
        try:
            with MachineOperations(config_for_db) as interface_connector:
                current_state = interface_connector.get_current_value_of_all_resources(machine_id)
            print(current_state)
            current_water_ml = current_state[2]
            current_milk_ml = current_state[3]
            current_coffee_gr = current_state[4]
            return current_water_ml, current_milk_ml, current_coffee_gr

        except Exception as e:
            print("Something went wrong: {}".format(e))
