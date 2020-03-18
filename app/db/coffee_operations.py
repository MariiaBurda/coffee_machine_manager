import mysql.connector

from config import config
from history_operations import get_all_history, get_last_orders
from machine_operations import fill_resources, get_current_state, change_current_state
from receipt_operations import get_receipt_info


def make_coffee(machine_id, receipt_id):
    current_water_ml, current_milk_ml, current_coffee_gr = current_resources_value(machine_id)
    receipt_water_ml, receipt_milk_ml, receipt_coffee_gr = receipt_resources_value(machine_id, receipt_id)

    coffee_is_ready = False

    while not coffee_is_ready:
        if current_water_ml >= receipt_water_ml \
                and current_milk_ml >= receipt_milk_ml \
                and current_coffee_gr >= receipt_coffee_gr:
            change_current_state(machine_id, receipt_water_ml, receipt_milk_ml, receipt_coffee_gr)
            print("Your coffee is ready")
            coffee_is_ready = True
        else:
            print("Not enough resources. Please fill resources")
            fill_resources(machine_id)
            current_water_ml, current_milk_ml, current_coffee_gr = current_resources_value(machine_id)
            continue


def current_resources_value(machine_id):
    current_state = get_current_state(machine_id)
    print(current_state)
    current_water_ml = current_state[2]
    current_milk_ml = current_state[3]
    current_coffee_gr = current_state[4]
    return current_water_ml, current_milk_ml, current_coffee_gr


def receipt_resources_value(machine_id, receipt_id):
    receipt = get_receipt_info(machine_id, receipt_id)
    print(receipt)
    receipt_water_ml = receipt[3]
    receipt_milk_ml = receipt[4]
    receipt_coffee_gr = receipt[5]

    return receipt_water_ml, receipt_milk_ml, receipt_coffee_gr


