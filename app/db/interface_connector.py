import mysql.connector


class InterfaceConnector:
    def __init__(self, db_config):
        self.config_for_db = db_config
        self.data = ()
        self.sql = ""

    def __enter__(self):
        self.db = mysql.connector.Connect(**self.config_for_db)
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):

        self.cursor.close()
        self.db.close()
