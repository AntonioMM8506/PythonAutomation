from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import time

class RunChromeTests():
    def test_chrome(self):
        # Set the path to the chromedriver executable
        chromedriver_path = 'drivers/chromedriver.exe'
        chrome_service = ChromeService(executable_path=chromedriver_path)

        # Instantiate the Chrome WebDriver
        driver = webdriver.Chrome(service = chrome_service)
        driver.get('https://www.google.com')

        # Sleep for 5 seconds to keep the browser open before it closes automatically. You can adjust the sleep time as needed.
        time.sleep(5) 

chrome_test = RunChromeTests()
chrome_test.test_chrome() # Chrome automatically closes after the test is done. Because the Chrome WebDriver is designed to close the browser when the test method finishes executing. If you want to keep the browser open, you can add a wait or a breakpoint at the end of the test method.
