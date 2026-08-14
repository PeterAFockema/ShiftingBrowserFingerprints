import unittest
from shiftingbrowserfingerprints.scrapers import return_Firefox_scrapers

class TestFunctions(unittest.TestCase):

    def test_return_Scrapers_object(self):
        return_Firefox_scrapers(self)

if __name__ == '__main__':
    unittest.main()
