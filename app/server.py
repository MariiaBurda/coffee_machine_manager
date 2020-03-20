import eventlet
import socketio

from app.db.history_operations import get_last_orders, get_statistic_of_used_resources
from app.db.machine_operations import fill_resources
from app.db.coffee_operations import make_coffee
from app.db.receipt_operations import get_receipts_list

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
    receipts_list = get_receipts_list()
    print('getting receipts_list, length: %s' % len(receipts_list))
    sio.emit('show_receipts_list', receipts_list)
    print('end execution of show_receipts_list')


@sio.event
def show_history(sid):
    print('start execution of show_history')
    last_orders = get_last_orders(machine_id, 10)
    print('getting %s last orders' % len(last_orders))
    mapped_orders = list(map(lambda x: (x[0], x[1].strftime("%m/%d/%Y, %H:%M:%S")), last_orders))
    sio.emit('show_history', mapped_orders)
    print('end execution of show_history')


@sio.event
def show_statistic_of_the_amount_of_coffee_drunk(sid):
    print('start execution of show_statistic_of_the_amount_of_coffee_drunk')
    list_of_the_amount_of_coffee_drunk = get_statistic_of_used_resources(machine_id)
    print('getting list_of_the_amount_of_coffee_drunk')
    sio.emit('show_statistic_of_the_amount_of_coffee_drunk', list_of_the_amount_of_coffee_drunk)
    print('end execution of show_statistic_of_the_amount_of_coffee_drunk')


@sio.event
def fill_resources_to_client(sid):
    print('start execution of fill_resources_to_client')
    fill_resources(machine_id)
    message_to_client = "Resources are filled"
    sio.emit('fill_resources_to_client', message_to_client)
    print('end execution of fill_resources_to_client')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
