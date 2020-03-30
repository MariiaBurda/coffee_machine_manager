import eventlet
import socketio

from db.config import config_for_db

from db.history_operations import HistoryOperations
from db.machine_operations import MachineOperations
from db.coffee_operations import make_coffee
from db.receipt_operations import ReceiptOperations
from db.db_helper import DbHelper

machine_id = 1

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def make_coffee_for_client(sid, receipt_id):
    print('start execution of make_coffee_for_client')
    result = make_coffee(machine_id, receipt_id)
    print(result)
    sio.emit('make_coffee_for_client', result)
    print('end execution of make_coffee_for_client')


@sio.event
def show_receipts_list(sid):
    print('start execution of show_receipts_list')
    with ReceiptOperations(config_for_db) as interface_connector:
        receipts_list = interface_connector.get_receipts_list()
    print('getting receipts_list, length: %s' % len(receipts_list))
    sio.emit('show_receipts_list', receipts_list)
    print('end execution of show_receipts_list')


@sio.event
def show_history(sid):
    print('start execution of show_history')
    with HistoryOperations(config_for_db) as interface_connector:
        last_orders = interface_connector.get_last_orders(machine_id, 10)
    print('getting %s last orders' % len(last_orders))
    sio.emit('show_history', last_orders)
    print('end execution of show_history')


@sio.event
def show_statistic_of_the_amount_of_coffee_drunk(sid):
    print('start execution of show_statistic_of_the_amount_of_coffee_drunk')
    with HistoryOperations(config_for_db) as interface_connector:
        list_of_the_amount_of_coffee_drunk = interface_connector.get_statistic_of_used_resources(machine_id)
    print('getting list_of_the_amount_of_coffee_drunk')
    sio.emit('show_statistic_of_the_amount_of_coffee_drunk', list_of_the_amount_of_coffee_drunk)
    print('end execution of show_statistic_of_the_amount_of_coffee_drunk')


@sio.event
def show_current_resources_value(sid):
    print('start execution of show_current_resources_value')
    with MachineOperations(config_for_db) as interface_connector:
        list_of_current_value_of_all_resources = list(interface_connector.get_current_value_of_all_resources(machine_id))
    print('getting list_of_current_value_of_all_resources')
    sio.emit('show_current_resources_value', list_of_current_value_of_all_resources)
    print('end execution of show_current_resources_value')


@sio.event
def fill_resources_to_client(sid):
    print('start execution of fill_resources_to_client')
    with MachineOperations(config_for_db) as interface_connector:
        interface_connector.fill_resources(machine_id)
    message_to_client = "Resources are filled"
    sio.emit('fill_resources_to_client', message_to_client)
    print('end execution of fill_resources_to_client')


@sio.event
def pass_db_sys(sid, db_sys):
    print('start execution of pass_db_sys')
    DbHelper.set_db_system(db_sys)
    print('end execution of pass_db_sys')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
