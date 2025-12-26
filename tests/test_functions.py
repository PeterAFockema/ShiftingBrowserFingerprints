import unittest
from shiftingbrowserfingerprints.functions import add

class TestFunctions(unittest.TestCase):

    def test_add_one(self):
        self.assertEqual(11, add(5, 6))

if __name__ == '__main__':
    unittest.main()
