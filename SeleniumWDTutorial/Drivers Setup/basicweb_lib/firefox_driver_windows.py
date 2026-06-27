from selenium import webdriver
import time

class RunFFTests():
    def test_ff(self):
        driver = webdriver.Chrome()
        driver.get('https://www.google.com')
        time.sleep(5) 

ff_test = RunFFTests()
ff_test.test_ff()