from app.server import history_operations, machine_operations, receipt_operations


def make_coffee(machine_id, receipt_id):
    try:
        current_water_ml, current_milk_ml, current_coffee_gr = machine_operations.pull_out_current_value_of_each_resource(machine_id)
        print('pull_out_current_value_of_each_resource finished')
        receipt_water_ml, receipt_milk_ml, receipt_coffee_gr = receipt_operations.get_receipt_resources_value(machine_id, receipt_id)
        print('get_receipt_resources_value finished')

        if current_water_ml >= receipt_water_ml \
                and current_milk_ml >= receipt_milk_ml \
                and current_coffee_gr >= receipt_coffee_gr:
            machine_operations.change_current_value_of_used_resources(machine_id, receipt_water_ml, receipt_milk_ml, receipt_coffee_gr)
            history_operations.add_order_to_history(machine_id, receipt_id)
            return True
        else:
            return False

    except Exception as e:
        print("Something went wrong: {}".format(e))
