#/usr/bin/python
# Start
# Sometimes the program has or had unwritten objects and attrs and
# we want to skip those failures
# Modules
import unittest
import sys
import pytest


class SkipTest(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(True, False)
        
    @unittest.skip("Well we skip this one")
    def test_skiper(self):
        self.assertEqual(True, False)
    
    @unittest.skipIf(sys.version_info.minor == 4, "broken on 3.4")
    def skiper(self):
        self.assertEqual(True, False)
    
    @unittest.skipUnless(sys.platform.startswith('linux'), "broken unless on linux")
    def skiper(self):
        self.assertEqual(False, True)



if __name__ == "__main__":
    unittest.main()

# End