import unittest
import pytest
from AutomationFramework.pages.courses_page import CoursesPage
from AutomationFramework.pages.login_page import LoginPage
from AutomationFramework.pages.navigation_menu import NavigationMenu
from ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt # This decorator is used to indicate that the test class will use data-driven testing.
class CoursesTestsMultipleData(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, self.baseURL)
        self.cp = CoursesPage(self.driver, self.baseURL)
        self.nav = NavigationMenu(self.driver)

    def setUp(self):
        self.nav.clickAllCourses()

    @pytest.mark.run(order=1)
    # This decorator is used to specify the order in which the test methods should be executed.
    @data(("JavaScript", "4111111111111111", "12/30", "123"), ("Rest API", "4222222222222222", "11/29", "456"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNumber, ccExp, ccCVV):
        self.cp.searchCourse(courseName)
        assert self.cp.selectCourse(courseName)
        self.cp.enroll()
        self.cp.enterCardNum(ccNumber)
        self.cp.enterCardExp(ccExp)
        self.cp.enterCardCVV(ccCVV)
        self.cp.buy()
        assert self.cp.verifyEnrollMessageDisplayed()