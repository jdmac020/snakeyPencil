import unittest
from paper_tests import PaperTests

suite1 = unittest.TestLoader().loadTestsFromTestCase(PaperTests)

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite1)