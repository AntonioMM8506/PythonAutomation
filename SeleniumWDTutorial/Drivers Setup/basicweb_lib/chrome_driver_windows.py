from selenium import webdriver
import time

class RunChromeTests():
    def test_chrome(self):
        driver = webdriver.Firefox()
        driver.get('https://www.google.com')
        time.sleep(5) 

chrome_test = RunChromeTests()
chrome_test.test_chrome() 