import unittest
from finalproj import MainWindow

class TestBudgetFunctions(unittest.TestCase):

    def setUp(self):
        self.main_window = MainWindow()

    def test_calculateBudget(self):
        self.main_window.entry.insert(0, '1000')  # Simulate user input
        self.main_window.calculateBudget()
        expected_output = "Total Budget: $1000.00\nSpending Money: $500.00"
        self.assertEqual(self.main_window.textBox.get("1.0", "end-1c"), expected_output)

    def test_viewBudgetPlan(self):
        self.main_window.entry.insert(0, '1000')  # Simulate user input
        self.main_window.viewBudgetPlan()
        expected_output = "Total Budget\t\t: $1000.00\nSpending Money\t\t: $500.00 \
            \nTo Save\t\t: $300.00\nExtra\t\t: $200.00"
        self.assertEqual(self.main_window.textBox.get("1.0", "end-1c"), expected_output)

    # Add more test cases for other functions as needed

if __name__ == '__main__':
    unittest.main()








