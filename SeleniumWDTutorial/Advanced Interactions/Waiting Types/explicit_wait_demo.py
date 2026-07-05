from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from explicit_wait_type import ExplicitWaitType

class ExplicitWaitDemo:
    def test(self):
        baseURL = "https://www.letskodeit.com/login"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        wait = ExplicitWaitType(driver)

        emailInput = driver.find_element(By.ID, "email")
        passwordInput = driver.find_element(By.ID, "login-password")

        emailInput.send_keys("test@email.com")
        passwordInput.send_keys("abcabc")
        loginButton = wait.wait_for_element(locator="login", locator_type="id", timeout=10, poll_frequency=0.5)
        loginButton.click()

        time.sleep(3)
        driver.quit()

cc = ExplicitWaitDemo()
cc.test()