#!/usr/bin/python
# Start
# Working on moneky Patching
# Modules
from numpy import array
import unittest


class TestMean(unittest.TestCase):
    
    def test_mean(self):
        self.assertEqual(array(1, 2, 3, 4, 5), 1)
    

if __name__ == "__main__":
    unittest.main()




# End