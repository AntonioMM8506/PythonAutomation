from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from handy_wrappers import HandyWrappers

class UsingWrappers():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        # The HandyWrappers class is a custom wrapper class that provides convenient methods for interacting with web elements.
        handyWrappers = HandyWrappers(driver)

        # The getElement method of the HandyWrappers class is used to retrieve a web element based on the provided locator and locator type.
        # It takes the locator and locator type as arguments and returns the corresponding web element.
        textField = handyWrappers.getElement("name")
        textField.send_keys("test")
        time.sleep(2)

        textField2 = handyWrappers.getElement("//input[@id='name']", "xpath")
        textField2.clear()
        time.sleep(2)

        driver.quit()

ff = UsingWrappers()
ff.test()