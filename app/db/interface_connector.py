import mysql.connector


class InterfaceConnector:
    def __init__(self, db_config):
        self.config_for_db = db_config

    def __enter__(self):
        self.db = mysql.connector.Connect(**self.config_for_db)
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')
        self.cursor.close()
        self.db.close()
