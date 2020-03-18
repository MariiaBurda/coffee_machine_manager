import eventlet
import socketio

from app.db.history_operations import get_last_orders

machine_id = 1

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def my_message(sid, data):
    print('message ', data)


@sio.event
def show_history(sid):
    print('start execution of show_history')
    last_orders = get_last_orders(machine_id, 10)
    print('getting %s last orders' % len(last_orders))
    mapped_orders = list(map(lambda x: (x[0], x[1].strftime("%m/%d/%Y, %H:%M:%S")), last_orders))
    sio.emit('show_history', mapped_orders)
    print('end execution of show_history')


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
