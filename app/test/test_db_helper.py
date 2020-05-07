import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))  # or sys.path.append('./')

from operations.db_helper import DbHelper


class TestDbHelper(unittest.TestCase):
    # setUp method is overridden from the parent class TestCase
    def setUp(self):
        self.db_helper = DbHelper()

    def test_set_db_system(self):
        # Arrange
        db_sys = 'mysql'
        # Act
        self.db_helper.set_db_system(db_sys)
        # Assert
        self.assertEqual(self.db_helper.db_system, 'mysql')

    def test_get_db_system(self):
        # Arrange
        db_sys = 'sqlite'
        # Act
        self.db_helper.set_db_system(db_sys)
        get_db = self.db_helper.get_db_system()
        # Assert
        self.assertEqual(get_db, 'sqlite')


if __name__ == "__main__":
    unittest.main()
