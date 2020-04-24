import unittest
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from operations.coffee_operations import make_coffee
from operations.machine_operations import MachineOperations
from operations.receipt_operations import ReceiptOperations
from operations.history_operations import HistoryOperations


class TestMakeCoffee(unittest.TestCase):
    @patch('operations.machine_operations.MachineOperations.pull_out_current_value_of_each_resource', return_value=(200, 300, 400))
    @patch('operations.receipt_operations.ReceiptOperations.get_receipt_resources_value', return_value=(5, 5, 5))
    @patch('operations.machine_operations.MachineOperations.change_current_value_of_used_resources', return_value=None)
    @patch('operations.history_operations.HistoryOperations.add_order_to_history', return_value=None)
    def test_make_coffee_check_return_true(self, pull_out_current_value_of_each_resource, get_receipt_resources_value, change_current_value_of_used_resources, add_order_to_history):
        # Arrange
        machine_id = 1
        receipt_id = 1
        # Act
        machine_operations = MachineOperations()
        receipt_operations = ReceiptOperations()
        history_operations = HistoryOperations()
        # Assert
        self.assertTrue(make_coffee(machine_id, receipt_id, history_operations, machine_operations, receipt_operations))

    @patch('operations.machine_operations.MachineOperations.pull_out_current_value_of_each_resource', return_value=(200, 300, 400))
    @patch('operations.receipt_operations.ReceiptOperations.get_receipt_resources_value', return_value=(500, 5, 5))
    @patch('operations.machine_operations.MachineOperations.change_current_value_of_used_resources', return_value=None)
    @patch('operations.history_operations.HistoryOperations.add_order_to_history', return_value=None)
    def test_make_coffee_check_return_false(self, pull_out_current_value_of_each_resource, get_receipt_resources_value, change_current_value_of_used_resources, add_order_to_history):
        # Arrange
        machine_id = 1
        receipt_id = 1
        # Act
        machine_operations = MachineOperations()
        receipt_operations = ReceiptOperations()
        history_operations = HistoryOperations()
        # Assert
        self.assertFalse(make_coffee(machine_id, receipt_id, history_operations, machine_operations, receipt_operations))

    @patch('operations.machine_operations.MachineOperations.pull_out_current_value_of_each_resource', return_value=None)
    @patch('operations.receipt_operations.ReceiptOperations.get_receipt_resources_value', return_value=(500, 5, 5))
    @patch('operations.machine_operations.MachineOperations.change_current_value_of_used_resources', return_value=None)
    @patch('operations.history_operations.HistoryOperations.add_order_to_history', return_value=None)
    def test_make_coffee_check_exception(self, pull_out_current_value_of_each_resource, get_receipt_resources_value, change_current_value_of_used_resources, add_order_to_history):
        # Arrange
        machine_id = 1
        receipt_id = 1
        # Act
        machine_operations = MachineOperations()
        receipt_operations = ReceiptOperations()
        history_operations = HistoryOperations()
        # Assert
        self.assertRaises(Exception, make_coffee(machine_id, receipt_id, history_operations, machine_operations, receipt_operations))


if __name__ == "__main__":
    unittest.main()
