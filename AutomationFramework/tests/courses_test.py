import unittest

import pytest

from AutomationFramework.pages.courses_page import CoursesPage
from AutomationFramework.pages.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class CoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, self.baseURL)
        self.cp = CoursesPage(self.driver, self.baseURL)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.lp.open(self.lp.url)
        self.lp.login("test@email.com", "abcabc")
        assert self.lp.verifyLoginSuccesful()
        
        self.cp.open(self.cp.url)
        self.cp.searchCourse("JavaScript")
        assert self.cp.selectCourse("JavaScript")
        self.cp.enroll()
        self.cp.enterCardNum("4111111111111111")
        self.cp.enterCardExp("12/30")
        self.cp.enterCardCVV("123")
        self.cp.buy()
        assert self.cp.verifyEnrollMessageDisplayed()