import unittest
from AutomationFramework.tests.login_test import LoginTests
from AutomationFramework.tests.courses_test_multiple_data_csv import CoursesTestsMultipleDataCSV
from AutomationFramework.tests.courses_test_multiple_data import CoursesTestsMultipleData
from AutomationFramework.tests.courses_test import CoursesTests

# This code imports the necessary modules and test classes for running a suite of tests.
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CoursesTestsMultipleDataCSV)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CoursesTestsMultipleData)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CoursesTests)

# This code creates a test suite that includes all the test cases from the specified test classes. 
# It then runs the test suite using a text-based test runner with verbosity level 2, which provides 
# detailed output of the test results.
suite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner(verbosity=2).run(suite)