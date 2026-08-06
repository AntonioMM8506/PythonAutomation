from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    # Locators
    _email_field_locator = (By.ID, "email")
    _password_field_locator = (By.ID, "login-password")
    _login_button_locator = (By.ID, "login")

    def get_email_field(self):
        return self.driver.find_element(*self._email_field_locator)

    def get_password_field(self):
        return self.driver.find_element(*self._password_field_locator)

    def get_login_button(self):
        return self.driver.find_element(*self._login_button_locator)

    # Transaction methods
    def login(self, username, password):
        self.get_email_field().clear()
        self.get_email_field().send_keys(username)
        self.get_password_field().clear()
        self.get_password_field().send_keys(password)
        self.get_login_button().click()