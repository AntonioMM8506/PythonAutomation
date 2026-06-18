from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FFService
import time

class RunFFTests():
    def test_ff(self):
        # Set the path to the geckodriver executable
        geckodriver_path = 'drivers/geckodriver.exe'
        ff_service = FFService(executable_path=geckodriver_path)

        # Instantiate the Firefox WebDriver
        driver = webdriver.Firefox(service = ff_service)
        driver.get('https://www.google.com')
        
        # Sleep for 5 seconds to keep the browser open before it closes automatically. You can adjust the sleep time as needed.
        time.sleep(5) 

ff_test = RunFFTests()
ff_test.test_ff() # Firefox remains open after the test is done. You can close it manually or add driver.quit() at the end of the test method to close it automatically.