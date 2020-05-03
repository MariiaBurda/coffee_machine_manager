import mysql.connector
import sqlite3

from run_db import db_path


class BaseConnector:
    def __init__(self):
        self.symbol = None
        self.time = None
        self.db = None
        self.cursor = None


class MySQLConnector(BaseConnector):
    def __init__(self, config_for_db):
        BaseConnector.__init__(self)
        self.symbol = '%s'
        self.time = "NOW()"
        self.config_for_db = config_for_db

    def connect(self):
        self.db = mysql.connector.Connect(**self.config_for_db)
        self.cursor = self.db.cursor()


class SQLiteConnector(BaseConnector):
    def __init__(self):
        BaseConnector.__init__(self)
        self.symbol = '?'
        self.time = "strftime('%d-%m-%Y %H:%M:%S', 'now')"

    def connect(self):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()


class Closing:
    def __init__(self, connector):
        self.connector = connector

    def __enter__(self):
        self.connector.connect()
        return self.connector

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')
        self.connector.cursor.close()
        self.connector.db.close()
