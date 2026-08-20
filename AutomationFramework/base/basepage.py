import logging

from AutomationFramework.base.selenium_driver import SeleniumDriver
from AutomationFramework.utilities.custom_logger import customLogger


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = customLogger(logging.INFO)

    def open(self, url):
        self.driver.get(url)

    def click(self, locator, locator_type="id"):
        self.elementClick(locator, locator_type)

    def type(self, locator, locator_type="id", value=""):
        self.sendKeys(locator, locator_type, value)

    def is_element_present(self, locator, locator_type="id"):
        return self.isElementPresent(locator, locator_type)

    def screenshot(self, result_message):
        self.screenShot(result_message)