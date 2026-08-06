from selenium import webdriver
from AutomationFramework.pages.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):
    
    def test_validLogin(self):
        baseURL = "https://www.letskodeit.com/login"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        lp = LoginPage(driver)
        lp.login("test@email.com", "abcabc")

