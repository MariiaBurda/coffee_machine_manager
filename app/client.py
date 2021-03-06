import socketio
import os

sio = socketio.Client()


@sio.event
def make_coffee_for_client(data):
    if data:
        print("Your coffee is ready")
    else:
        print("Not enough resources. Please fill resources")

    print_back()
    process_back()


@sio.event
def show_receipts_list(data):
    for item in data:
        print(str(item[0]) + '. ' + str(item[1]))

    receipt_id = int(input())
    sio.emit('make_coffee_for_client', receipt_id)


@sio.event
def show_history(data):
    for item in data:
        print(str(item[0]) + ': ' + str(item[1]))

    print_back()
    process_back()


@sio.event
def show_statistic_of_the_amount_of_coffee_drunk(data):
    for item in data:
        print(item[0], '-', item[1], 'orders')

    print_back()
    process_back()


@sio.event
def show_current_resources_value(data):
    current_water_ml = data[2]
    current_milk_ml = data[3]
    current_coffee_gr = data[4]
    print(f"Current resources value:\n\n"
          f"Water - {current_water_ml} ml\n"
          f"Milk - {current_milk_ml} ml\n"
          f"Coffee - {current_coffee_gr} gr")

    print_back()
    process_back()


@sio.event
def fill_resources_to_client(data):
    print(data)
    print_back()
    process_back()


@sio.event
def disconnect():
    pass


@sio.event
def connect():
    pass


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    cls()
    print("Choose what you want (enter a number)\n"
          "1. Make coffee\n"
          "2. Show history\n"
          "3. Show statistic of the amount of coffee drunk\n"
          "4. Show current resources value\n"
          "5. Fill resources\n"
          "6. Exit")


def print_back():
    print("\nEnter any button to go back")


def process_back():
    str(input())
    print_menu()
    process_command()


def process_command():
    cmd = str(input())

    if cmd == "1":
        cls()
        print("Choose which coffee you want (enter a number)")
        sio.emit('show_receipts_list')
    elif cmd == "2":
        cls()
        sio.emit('show_history')
    elif cmd == "3":
        cls()
        sio.emit('show_statistic_of_the_amount_of_coffee_drunk')
    elif cmd == "4":
        cls()
        sio.emit('show_current_resources_value')
    elif cmd == "5":
        cls()
        sio.emit('fill_resources_to_client')
    elif cmd == "6":
        sio.disconnect()
        print("Have a wonderful day :)")
    else:
        print("Unknown command. Please enter again")
        process_command()


if __name__ == '__main__':
    sio.connect('http://localhost:5000')
    print_menu()
    process_command()
