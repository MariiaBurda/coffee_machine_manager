import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def make_coffee_for_client(data):
    if data:
        print("Your coffee is ready")
    else:
        print("Not enough resources. Please fill resources")


@sio.event
def show_receipts_list(data):
    for item in data:
        print(item)


@sio.event
def show_history(data):
    for item in data:
        print(item)


@sio.event
def fill_resources_to_client(data):
    print(data)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')

while True:
    print("Choose what you want (enter a number)")
    print("1. Make coffee")
    print("2. Show history")
    print("3. Fill resources")
    print("4. Exit")

    cmd = str(input())

    if cmd == "1":
        print("Choose which coffee you want (enter a number)")
        sio.emit('show_receipts_list')
        receipt_id = int(input())
        sio.emit('make_coffee_for_client', receipt_id)
    elif cmd == "2":
        sio.emit('show_history')
    elif cmd == "3":
        sio.emit('fill_resources_to_client')
    elif cmd == "4":
        sio.disconnect()
        print("have a nice day")
        break
    else:
        print("Unknown command. Please enter again")
