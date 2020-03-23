from .config import config_for_db
from .interface_connector import InterfaceConnector


class FillResources(InterfaceConnector):
    def fill_resources(self, machine_id):
        self.sql = "UPDATE machine " \
              "SET current_water_ml = max_water_ml, " \
              "current_milk_ml = max_milk_ml, " \
              "current_coffee_gr = max_coffee_gr " \
              "WHERE id = %s"
        self.data = (machine_id,)
        self.cursor.execute(self.sql, self.data)

        self.db.commit()


class GetCurrentValueOfAllResources(InterfaceConnector):
    def __init__(self, db_config):
        InterfaceConnector.__init__(self, db_config)
        self.row = []

    def get_current_value_of_all_resources(self, machine_id):
        self.sql = "SELECT id, name, current_water_ml, current_milk_ml, current_coffee_gr " \
              "FROM machine " \
              "WHERE id = %s"
        self.data = (machine_id,)
        self.cursor.execute(self.sql, self.data)
        self.row = self.cursor.fetchone()

        return self.row


def pull_out_current_value_of_each_resource(machine_id):
    try:
        with GetCurrentValueOfAllResources(config_for_db) as interface_connector:
            current_state = interface_connector.get_current_value_of_all_resources(machine_id)
        print(current_state)
        current_water_ml = current_state[2]
        current_milk_ml = current_state[3]
        current_coffee_gr = current_state[4]
        return current_water_ml, current_milk_ml, current_coffee_gr

    except Exception as e:
        print("Something went wrong: {}".format(e))


class ChangeCurrentValueOfUsedResources(InterfaceConnector):
    def change_current_value_of_used_resources(self, machine_id, water_ml, milk_ml, coffee_gr):
        self.sql = "UPDATE machine " \
                   "SET current_water_ml = current_water_ml - %s, " \
                   "current_milk_ml = current_milk_ml - %s, " \
                   "current_coffee_gr = current_coffee_gr - %s " \
                   "WHERE id = %s"
        self.data = (water_ml, milk_ml, coffee_gr, machine_id)
        self.cursor.execute(self.sql, self.data)

        self.db.commit()
