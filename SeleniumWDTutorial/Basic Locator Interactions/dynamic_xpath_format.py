from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DynamicXpathFormat():
    def test(self):
        baseURL = "https://www.letskodeit.com/login"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        

        # Example: Locating a button element with a dynamic ID
        loginButton = driver.find_element(By.ID, "login")
        email = driver.find_element(By.ID, "email")
        password = driver.find_element(By.ID, "login-password")

        email.send_keys("test@email.com")
        password.send_keys("abcabc")
        loginButton.click()
        time.sleep(2)

        # Dynamic XPath format is used to locate web elements whose attributes or values may change dynamically.
        # It allows you to create flexible and reusable XPath expressions that can adapt to different scenarios.
        # The format method is used to insert dynamic values into the XPath expression.
        # underscore (_) is used to indicate that the value will be provided dynamically at runtime.
        _course = "//*[@id='course-list']//*[contains(text(), '{0}')]"
        _courseLocator = _course.format("Java Step By Step For Testers")
        courseElement = driver.find_element(By.XPATH, _courseLocator)
        courseElement.click()
        time.sleep(2)

        driver.quit()

cc = DynamicXpathFormat()
cc.test()