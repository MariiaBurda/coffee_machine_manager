from .db_helper import DbHelper
from .interface_connector import MySQLConnector, SQLiteConnector
from .base_mapper import MySQLMapper, SQLiteMapper
from .config import config_for_db


class BaseOperation:
    def __init__(self):
        self.connector = None
        self.mapper = None
        self.initialize()

    def initialize(self):
        db_sys = DbHelper.get_db_system()
        if db_sys == 'mysql':
            self.connector = MySQLConnector(config_for_db)
            self.mapper = MySQLMapper()
        elif db_sys == 'sqlite':
            self.connector = SQLiteConnector()
            self.mapper = SQLiteMapper()
