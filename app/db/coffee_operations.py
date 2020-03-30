from .config import config_for_db

from .history_operations import HistoryOperations
from .machine_operations import MachineOperations
from .receipt_operations import ReceiptOperations


def make_coffee(machine_id, receipt_id):
    try:
        current_water_ml, current_milk_ml, current_coffee_gr = MachineOperations.pull_out_current_value_of_each_resource(machine_id)
        print('pull_out_current_value_of_each_resource finished')
        receipt_water_ml, receipt_milk_ml, receipt_coffee_gr = ReceiptOperations.get_receipt_resources_value(machine_id, receipt_id)
        print('get_receipt_resources_value finished')

        if current_water_ml >= receipt_water_ml \
                and current_milk_ml >= receipt_milk_ml \
                and current_coffee_gr >= receipt_coffee_gr:
            with MachineOperations(config_for_db) as interface_connector:
                interface_connector.change_current_value_of_used_resources(machine_id, receipt_water_ml, receipt_milk_ml, receipt_coffee_gr)
            with HistoryOperations(config_for_db) as interface_connector:
                interface_connector.add_order_to_history(machine_id, receipt_id)
            return True
        else:
            return False

    except Exception as e:
        print("Something went wrong: {}".format(e))
