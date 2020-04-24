import datetime
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from operations.base_mapper import MySQLMapper, SQLiteMapper


class TestMySQLMapper(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.mysql_mapper = MySQLMapper()

    def test_map_orders_check_return_type(self):
        # Arrange
        rows = [('Americano', datetime.datetime(2020, 4, 16, 22, 18, 7)),
                ('Latte', datetime.datetime(2020, 4, 10, 16, 29, 59))]
        # Act
        mapped_orders = self.mysql_mapper.map_orders(rows)
        # Assert
        self.assertIsInstance(mapped_orders, list)

    def test_map_orders_check_return_date_format(self):
        # Arrange
        rows = [('Americano', datetime.datetime(2020, 4, 16, 22, 18, 7)),
                ('Latte', datetime.datetime(2020, 4, 10, 16, 29, 59))]
        # Act
        mapped_orders = self.mysql_mapper.map_orders(rows)
        # Assert
        self.assertEqual(mapped_orders, [('Americano', '16-04-2020, 22:18:07'),
                                         ('Latte', '10-04-2020, 16:29:59')])


if __name__ == "__main__":
    unittest.main()
