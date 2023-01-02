import unittest
import io
import sys
from utils.displays import print_items_found


class PrintItemsFoundTest(unittest.TestCase):
    def test_multiple_items_list(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_items_found(["value1", "value2", "value3"], "values")
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "value1\nvalue2\nvalue3")

    
    def test_one_item_list(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_items_found(["value1"], "values")
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "value1")

    
    def test_no_item_list_with_plural_given(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_items_found([], "values")
        sys.stdout = sys.__stdout__

        self.assertEqual(captured_output.getvalue().strip(), "No values were found")

    
    def test_no_item_list_without_plural_given(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print_items_found([])
        sys.stdout = sys.__stdout__
        
        self.assertEqual(captured_output.getvalue().strip(), "No items were found")
