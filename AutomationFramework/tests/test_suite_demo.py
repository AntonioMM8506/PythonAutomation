import unittest
from AutomationFramework.tests.login_test import LoginTests
from AutomationFramework.tests.courses_test_multiple_data_csv import CoursesTestsMultipleDataCSV
from AutomationFramework.tests.courses_test_multiple_data import CoursesTestsMultipleData
from AutomationFramework.tests.courses_test import CoursesTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CoursesTestsMultipleDataCSV)
tc3 = unittest.TestLoader().loadTestsFromTestCase(CoursesTestsMultipleData)
tc4 = unittest.TestLoader().loadTestsFromTestCase(CoursesTests)

suite = unittest.TestSuite([tc1, tc2, tc3, tc4])

unittest.TextTestRunner(verbosity=2).run(suite)