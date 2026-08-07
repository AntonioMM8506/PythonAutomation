import pytest
from selenium import webdriver
from AutomationFramework.pages.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.lp = LoginPage(self.driver)
        self.driver.get("https://www.letskodeit.com/login")

    def tearDown(self):
        self.driver.quit()

    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        assert self.lp.verifyLoginSuccesful()

    def test_invalidLogin(self):
        self.lp.login("test@email.com", "wrongpassword")
        assert self.lp.verifyLoginFailed()