from selenium import webdriver
import time


class RunSafariTests():
    def test_safari(self):
        driver = webdriver.Safari()
        driver.get('https://www.google.com')
        time.sleep(5) 

safari_test = RunSafariTests()
safari_test.test_safari()