"""
Sample Tests

"""

from django.test import SimpleTestCase
from app import calc

class calcTests(SimpleTestCase):
    """Test the calc functions"""

    def test_add_nums(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(3, 8), 11)

    def test_subtract_nums(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(calc.subtract(5, 11), 6)   
