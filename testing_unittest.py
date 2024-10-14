"""
This test runnes and checkes if the provided condition are true and display the time taken to run the test checker \n
"""

import unittest

def add(x,y):
    return x + y

def multiply(x,y):
    return x * y

class Testing(unittest.TestCase):

    def test_add_positive(self):
        result = add(5,6)
        self.assertEqual(result, 11)

    def test_add_negative(self):
        result = add(-2, 7)
        self.assertEqual(result, 5)
    
    def test_multiply_positive(self):
        result = multiply(2,3)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()