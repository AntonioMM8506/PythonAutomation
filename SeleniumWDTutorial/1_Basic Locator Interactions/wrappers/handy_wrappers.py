from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HandyWrappers():

    def __init__(self, driver):
        self.driver = driver

    # This method is used to get the By type based on the locator type provided.
    # It takes the locator type as an argument and returns the corresponding By type.
    def getBYType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            print("Locator type " + locatorType + " not correct/supported")
        return False


    def get_by_type(self, locatorType):
        return self.getBYType(locatorType)

    # This method is used to get a web element based on the locator and locator type provided.
    # It takes the locator and locator type as arguments and returns the corresponding web element.
    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            byType = self.getBYType(locatorType)
            element = self.driver.find_element(byType, locator)
            print("Element found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            print("Element not found with locator: " + locator + " and locatorType: " + locatorType)
        return element


    # This method is used to check if a web element is present based on the locator and locator type provided.
    # It takes the locator and locator type as arguments and returns a boolean indicating whether the element is present.
    def isElementPresent(self, locator, byType="id"):
        try:
            element = self.driver.find_element(byType, locator)
            if element is not None:
                print("Element present with locator: " + locator)
                return True
            else:
                print("Element not present with locator: " + locator)
                return False
        except:
            print("Element not found with locator: " + locator)
            return False
        
    def areElementsPresent(self, locator, byType="id"):
        try:
            elements = self.driver.find_elements(byType, locator)
            if len(elements) > 0:
                print("Elements present with locator: " + locator)
                return True
            else:
                print("Elements not present with locator: " + locator)
                return False
        except:
            print("Elements not found with locator: " + locator)
            return False