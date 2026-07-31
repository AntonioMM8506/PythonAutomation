import sys
import unittest
from pathlib import Path

# Add the parent directory of the current file to sys.path to allow importing modules 
# from that directory
sys.path.append(str(Path(__file__).resolve().parent))
from assert_methods import AssertMethodsDemo
from test_case_demo import TestCaseDemo


class TestSuiteDemo(unittest.TestCase):

    # Load test cases from the test classes
    ts1 = unittest.TestLoader().loadTestsFromTestCase(AssertMethodsDemo)
    ts2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)

    # Define a test suite that combines the test cases from both classes
    def test_suite(self):
        smoke_test_suite = unittest.TestSuite([self.ts1, self.ts2])
        unittest.TextTestRunner(verbosity=2).run(smoke_test_suite)

if __name__ == '__main__':
    unittest.main(verbosity=2)
