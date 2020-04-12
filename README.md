# Coffee_machine_manager
Simulation of a remote coffee machine management by python-socketio. Used Python 3.7.5
### Coffee_machine_manager_db_diagram


![coffee_machine_manager_db_diagram](https://user-images.githubusercontent.com/56352901/76962995-f0ee9f80-6928-11ea-9b0b-80deabacba98.png)

### Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Clone

- Clone this repo to your local machine using `https://github.com/MariiaBurda/coffee_machine_manager/`

### Setup

- If you want to use makefile, skip this step and go to Usage -- Option 2

> create and activate virtual environment first

```shell
$ python3 -m venv venv
$ . venv/bin/activate
```

> install all needed packages

```shell
$ pip install -r requirements.txt
```

> create and populate sqlite database

```shell
$ python app/run_db.py
```

> test database connection

```shell
$ python app/database/connection_testing/test_sqlite_db_connection.py
```


### Usage
- Option 1: 

> run server.py

```shell
$ python app/server.py
```

> open new terminal, activate virtual env and run client.py

```shell
$ . venv/bin/activate
$ python app/client.py
```
- Option 2: use makefile

> run make

```shell
$ make
```

> open new terminal and run make run_client

```shell
$ make run_client
```
