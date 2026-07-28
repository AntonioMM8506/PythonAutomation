from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class ClickAndSendKeys():
    def test(self):
        baseURL = "https://www.letskodeit.com/login"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        emailInput = driver.find_element(By.ID, "email")
        passwordInput = driver.find_element(By.ID, "login-password")

        emailInput.send_keys("test@email.com")
        passwordInput.send_keys("testpassword")
        
        # sleep method is used to pause the execution of the program for a specified amount of time. 
        # It takes the number of seconds as an argument and suspends the program's execution for that duration. 
        # This can be useful for waiting for certain elements to load or for observing the behavior of the application during testing.
        time.sleep(3)
        emailInput.clear()

        time.sleep(3)
        emailInput.send_keys("this is a test")


ff = ClickAndSendKeys()
ff.test()