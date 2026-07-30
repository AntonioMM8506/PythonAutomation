import unittest

class TestCaseDemo(unittest.TestCase):

    # decorator @classmethod is used to define a class method that is called before 
    # any tests in the class are run. 
    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("Setting up TestCaseDemo class...")
        print("#" * 30)

    def test_addition(self):
        self.assertEqual(1 + 1, 2)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

    @classmethod
    def tearDownClass(cls):
        print("#" * 30)
        print("Tearing down TestCaseDemo class...")
        print("#" * 30)

if __name__ == '__main__':
    # verbosity = 2 provides more detailed test output, including the name of 
    # each test and its result.
    unittest.main(verbosity=2)