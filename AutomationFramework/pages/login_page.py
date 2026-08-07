from selenium.webdriver.common.by import By
from AutomationFramework.base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _email_field_locator = (By.ID, "email")
    _password_field_locator = (By.ID, "login-password")
    _login_button_locator = (By.ID, "login")

    # Transaction methods
    def login(self, username, password):
        self.sendKeys(self._email_field_locator[1], self._email_field_locator[0], username)
        self.sendKeys(self._password_field_locator[1], self._password_field_locator[0], password)
        self.elementClick(self._login_button_locator[1], self._login_button_locator[0])

    def verifyLoginSuccesful(self):
        #userIcon = self.driver.find_element(By.ID, "dropdownMenu1")
        return self.isElementPresent("dropdownMenu1", "id")

    def verifyLoginFailed(self):
        return self.isElementPresent("//span[contains(text(),'Incorrect login details')]", "xpath")