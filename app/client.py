import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')


@sio.event
def show_history(data):
    for item in data:
        print(item)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:5000')

while True:
    print("Enter what you want")
    print("1. Make coffee")
    print("2. Show history")
    print("3. Fill resources")
    print("4. Exit")

    cmd = str(input())

    if cmd == "1":
        print("make coffee")
    elif cmd == "2":
        sio.emit('show_history')
    elif cmd == "3":
        print("fill resources")
    elif cmd == "4":
        sio.disconnect()
        print("have a nice day")
        break
    else:
        print("Unknown command. Please enter again")
