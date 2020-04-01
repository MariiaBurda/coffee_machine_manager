import eventlet
import socketio
import argparse

from app.db.history_operations import HistoryOperations
from app.db.machine_operations import MachineOperations
from app.db.receipt_operations import ReceiptOperations
from app.db import coffee_operations
from app.db.db_helper import DbHelper

machine_id = 1
print('start execution of history_operations')
history_operations = HistoryOperations()
print('end execution of history_operations\n')

print('start execution of machine_operations')
machine_operations = MachineOperations()
print('end execution of machine_operations\n')

print('start execution of receipt_operations')
receipt_operations = ReceiptOperations()
print('end execution of receipt_operations\n')

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
    result = coffee_operations.make_coffee(machine_id, receipt_id)
    print(result)
    sio.emit('make_coffee_for_client', result)
    print('end execution of make_coffee_for_client')


@sio.event
def show_receipts_list(sid):
    print('start execution of show_receipts_list')
    receipts_list = receipt_operations.get_receipts_list()
    print('getting receipts_list, length: %s' % len(receipts_list))
    sio.emit('show_receipts_list', receipts_list)
    print('end execution of show_receipts_list')


@sio.event
def show_history(sid):
    print('start execution of show_history')
    last_orders = history_operations.get_last_orders(machine_id, 10)
    print('getting %s last orders' % len(last_orders))
    sio.emit('show_history', last_orders)
    print('end execution of show_history')


@sio.event
def show_statistic_of_the_amount_of_coffee_drunk(sid):
    print('start execution of show_statistic_of_the_amount_of_coffee_drunk')
    list_of_the_amount_of_coffee_drunk = history_operations.get_statistic_of_used_resources(machine_id)
    print('getting list_of_the_amount_of_coffee_drunk')
    sio.emit('show_statistic_of_the_amount_of_coffee_drunk', list_of_the_amount_of_coffee_drunk)
    print('end execution of show_statistic_of_the_amount_of_coffee_drunk')


@sio.event
def show_current_resources_value(sid):
    print('start execution of show_current_resources_value')
    list_of_current_value_of_all_resources = list(machine_operations.get_current_value_of_all_resources(machine_id))
    print('getting list_of_current_value_of_all_resources')
    sio.emit('show_current_resources_value', list_of_current_value_of_all_resources)
    print('end execution of show_current_resources_value')


@sio.event
def fill_resources_to_client(sid):
    print('start execution of fill_resources_to_client')
    machine_operations.fill_resources(machine_id)
    message_to_client = "Resources are filled"
    sio.emit('fill_resources_to_client', message_to_client)
    print('end execution of fill_resources_to_client')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-dB", "--dbSystem", help="Db system.", type=str, default='sqlite')
    arg = parser.parse_args()

    return arg


def choose_db(db_system='sqlite'):
    if db_system == 'sqlite':
        return 'sqlite'
    elif db_system == 'mysql':
        return 'mysql'


def pass_db_sys(db_system):
    print('start execution of pass_db_sys')
    DbHelper.set_db_system(db_system)
    print('end execution of pass_db_sys')


if __name__ == '__main__':
    args = parse_arguments()
    db_sys = choose_db(args.dbSystem)
    print(f'chosen db sys: {db_sys}')
    pass_db_sys(db_sys)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
