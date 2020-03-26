import mysql.connector
import sqlite3
from.db_helper import DbHelper
from database.initialization.sqlite.run_db import db_path


class InterfaceConnector:
    def __init__(self, db_config):
        self.config_for_db = db_config

    def __enter__(self):
        self.db_sys = DbHelper.get_db_system()
        if self.db_sys == 'mysql':
            self.symbol = '%s'
            self.time = "NOW()"
            self.db = mysql.connector.Connect(**self.config_for_db)
        elif self.db_sys == 'sqlite':
            self.symbol = '?'
            self.time = "strftime('%d-%m-%Y %H:%M:%S', 'now')"
            self.db = sqlite3.connect(db_path)

        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')
        self.cursor.close()
        self.db.close()
