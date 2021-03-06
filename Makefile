.ONESHELL:

all: install run_db run_server run_client
.PHONY: all

install:
	echo "Creating virtualenv, installing packages"
	python3 -m venv venv
	. venv/bin/activate
	pip install -r requirements.txt
	
run_db:
	echo "Rinning sqlite database"
	. venv/bin/activate
	python app/run_db.py

run_server:
	echo "Running server.py module"
	. venv/bin/activate
	python app/server.py

run_client:
	echo "Running client.py module"
	. venv/bin/activate
	python app/client.py
