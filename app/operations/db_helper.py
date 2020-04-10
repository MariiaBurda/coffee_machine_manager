class DbHelper:
    db_system = 'sqlite'

    @classmethod
    def get_db_system(cls):
        return cls.db_system

    @classmethod
    def set_db_system(cls, db_sys):
        cls.db_system = db_sys
