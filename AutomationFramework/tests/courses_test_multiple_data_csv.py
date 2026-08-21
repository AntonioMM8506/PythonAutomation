import unittest
from pathlib import Path
import pytest
from AutomationFramework.pages.courses_page import CoursesPage
from AutomationFramework.pages.login_page import LoginPage
from AutomationFramework.utilities.read_csv_data import get_csv_data
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt # This decorator is used to indicate that the test class will use data-driven testing.
class CoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, self.baseURL)
        self.cp = CoursesPage(self.driver, self.baseURL)

    @pytest.mark.run(order=1)
    # This decorator is used to specify the order in which the test methods should be executed.
    # The @data decorator is used to provide multiple sets of data for the test method. Each tuple represents a set of input values for the test.
    # The @unpack decorator is used to unpack the tuples into individual arguments for the test
    @data(*get_csv_data(Path(__file__).resolve().parents[1] / "test-data" / "ccInfo.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNumber, ccExp, ccCVV):
        self.lp.open(self.lp.url)
        self.lp.login("test@email.com", "abcabc")
        assert self.lp.verifyLoginSuccesful()
        
        self.cp.open(self.cp.url)
        self.cp.searchCourse(courseName)
        assert self.cp.selectCourse(courseName)
        self.cp.enroll()
        self.cp.enterCardNum(ccNumber)
        self.cp.enterCardExp(ccExp)
        self.cp.enterCardCVV(ccCVV)
        self.cp.buy()
        assert self.cp.verifyEnrollMessageDisplayed()