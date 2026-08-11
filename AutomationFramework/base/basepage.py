import logging

from AutomationFramework.base.selenium_driver import SeleniumDriver
from AutomationFramework.utilities.custom_logger import customLogger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.selenium_driver = SeleniumDriver(driver)
        self.log = customLogger(logging.INFO)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator, locator_type="id"):
        self.selenium_driver.elementClick(locator, locator_type)

    def type(self, locator, locator_type="id", value=""):
        self.selenium_driver.sendKeys(locator, locator_type, value)

    def is_element_present(self, locator, locator_type="id"):
        return self.selenium_driver.isElementPresent(locator, locator_type)

    def screenshot(self, result_message):
        self.selenium_driver.screenShot(result_message)