from selenium.webdriver.common.by import By
from AutomationFramework.base.basepage import BasePage
from AutomationFramework.pages.navigation_menu import NavigationMenu


class LoginPage(BasePage):
    path = "/login"

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.driver = driver
        self.url = f"{base_url.rstrip('/')}" + self.path
        self.navigation_menu = NavigationMenu(self.driver)

    # Locators
    _email_field_locator = (By.ID, "email")
    _password_field_locator = (By.ID, "login-password")
    _login_button_locator = (By.ID, "login")

    # Transaction methods
    def login(self, username="", password=""):
        self.type(self._email_field_locator[1], self._email_field_locator[0], username)
        self.type(self._password_field_locator[1], self._password_field_locator[0], password)
        self.click(self._login_button_locator[1], self._login_button_locator[0])

    def verifyLoginSuccesful(self):
        return self.is_element_present("dropdownMenu1", "id")

    def verifyLoginFailed(self):
        return self.is_element_present("//span[contains(text(),'Incorrect login details')]", "xpath")