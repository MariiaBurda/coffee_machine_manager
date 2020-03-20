import sys

from .history_operations import add_order_to_history
from .machine_operations import pull_out_current_value_of_each_resource, change_current_value_of_used_resources
from .receipt_operations import get_receipt_resources_value


def make_coffee(machine_id, receipt_id):
    try:
        current_water_ml, current_milk_ml, current_coffee_gr = pull_out_current_value_of_each_resource(machine_id)
        receipt_water_ml, receipt_milk_ml, receipt_coffee_gr = get_receipt_resources_value(machine_id, receipt_id)

        if current_water_ml >= receipt_water_ml \
                and current_milk_ml >= receipt_milk_ml \
                and current_coffee_gr >= receipt_coffee_gr:
            change_current_value_of_used_resources(machine_id, receipt_water_ml, receipt_milk_ml, receipt_coffee_gr)
            add_order_to_history(machine_id, receipt_id)
            return True
        else:
            return False
    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))
