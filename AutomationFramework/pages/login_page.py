from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        username_field = self.driver.find_element(By.ID, "email")
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "login-password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.driver.find_element(By.ID, "login")
        login_button.click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()