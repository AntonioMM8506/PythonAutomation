
from AutomationFramework.pages.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ScreenshotTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver, self.baseURL)
        self.driver.get(self.lp.url)
        
    def test_screenshots(self):
        self.lp.login("test@email.com", "wrongpassword")
        assert self.lp.verifyLoginSuccesful()