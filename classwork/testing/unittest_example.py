import unittest
import math
 
class TestMath(unittest.TestCase):

    def setUp(self):
        pass
 
    def test_math_sqrt(self):
        self.assertEqual(math.sqrt(81), 124.0)
 
    def test_math_ceil_less_5(self):
        self.assertEqual(math.ceil(35.1), 36)
        
    def test_math_ceil_more_5(self):
        self.assertEqual(math.ceil(125.7), 126)
        
    def test_math_ceil_equal_5(self):
        self.assertEqual(math.ceil(0.5), 1)

unittest.main()
