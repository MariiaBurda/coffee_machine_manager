from .interface_connector import Closing
from .base_operation import BaseOperation


class MachineOperations(BaseOperation):
    def fill_resources(self, machine_id):
        with Closing(self.connector) as closing:
            sql = "UPDATE machine " \
                  "SET current_water_ml = max_water_ml, " \
                  "current_milk_ml = max_milk_ml, " \
                  "current_coffee_gr = max_coffee_gr " \
                  f"WHERE id = {closing.symbol}"
            data = (machine_id,)
            closing.cursor.execute(sql, data)

            closing.db.commit()

    def get_current_value_of_all_resources(self, machine_id):
        with Closing(self.connector) as closing:
            sql = "SELECT id, name, current_water_ml, current_milk_ml, current_coffee_gr " \
                  "FROM machine " \
                  f"WHERE id = {closing.symbol}"
            data = (machine_id,)
            closing.cursor.execute(sql, data)
            row = closing.cursor.fetchone()

            return row

    def change_current_value_of_used_resources(self, machine_id, water_ml, milk_ml, coffee_gr):
        with Closing(self.connector) as closing:
            sql = "UPDATE machine " \
                       f"SET current_water_ml = current_water_ml - {closing.symbol}, " \
                       f"current_milk_ml = current_milk_ml - {closing.symbol}, " \
                       f"current_coffee_gr = current_coffee_gr - {closing.symbol} " \
                       f"WHERE id = {closing.symbol}"
            data = (water_ml, milk_ml, coffee_gr, machine_id)
            closing.cursor.execute(sql, data)

            closing.db.commit()

    def pull_out_current_value_of_each_resource(self, machine_id):
        try:
            current_state = self.get_current_value_of_all_resources(machine_id)
            print(current_state)
            current_water_ml = current_state[2]
            current_milk_ml = current_state[3]
            current_coffee_gr = current_state[4]
            return current_water_ml, current_milk_ml, current_coffee_gr

        except Exception as e:
            print("Something went wrong: {}".format(e))
