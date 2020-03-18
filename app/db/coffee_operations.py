import mysql.connector
import sys

from .config import config
from .history_operations import get_all_history, get_last_orders, add_order_to_history
from .machine_operations import fill_resources, get_current_state, change_current_state
from .receipt_operations import get_receipt_info


def make_coffee(machine_id, receipt_id):
    try:
        current_water_ml, current_milk_ml, current_coffee_gr = current_resources_value(machine_id)
        receipt_water_ml, receipt_milk_ml, receipt_coffee_gr = receipt_resources_value(machine_id, receipt_id)

        if current_water_ml >= receipt_water_ml \
                and current_milk_ml >= receipt_milk_ml \
                and current_coffee_gr >= receipt_coffee_gr:
            change_current_state(machine_id, receipt_water_ml, receipt_milk_ml, receipt_coffee_gr)
            add_order_to_history(machine_id, receipt_id)
            return True
        else:
            return False
    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))


def current_resources_value(machine_id):
    try:
        current_state = get_current_state(machine_id)
        print(current_state)
        current_water_ml = current_state[2]
        current_milk_ml = current_state[3]
        current_coffee_gr = current_state[4]
        return current_water_ml, current_milk_ml, current_coffee_gr

    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))


def receipt_resources_value(machine_id, receipt_id):
    try:
        receipt = get_receipt_info(machine_id, receipt_id)
        print(receipt)
        receipt_water_ml = receipt[3]
        receipt_milk_ml = receipt[4]
        receipt_coffee_gr = receipt[5]

        return receipt_water_ml, receipt_milk_ml, receipt_coffee_gr

    except:
        print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                               sys.exc_info()[1],
                                               sys.exc_info()[2].tb_lineno))
