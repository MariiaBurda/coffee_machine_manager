class BaseMapper:
    @staticmethod
    def map_orders(rows):
        pass


class MySQLMapper(BaseMapper):
    @staticmethod
    def map_orders(last_orders):
        mapped_orders = list(map(lambda x: (x[0], x[1].strftime("%d-%m-%Y, %H:%M:%S")), last_orders))
        return mapped_orders


class SQLiteMapper(BaseMapper):
    @staticmethod
    def map_orders(last_orders):
        mapped_orders = last_orders
        return mapped_orders
