from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from handy_wrappers import HandyWrappers

class ElementsPresentCheck():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        # The HandyWrappers class is a custom wrapper class that provides convenient methods for interacting with web elements.
        handyWrappers = HandyWrappers(driver)

        # Check if elements are present using the isElementPresent method.
        elementResult = handyWrappers.isElementPresent("name")
        print("Is element present: " + str(elementResult))
        time.sleep(2)

        # Check if multiple elements are present using the areElementsPresent method.|
        elementsResults = handyWrappers.areElementsPresent("name")
        print("Are elements present: " + str(elementsResults)) 
        driver.quit()

ff = ElementsPresentCheck()
ff.test()