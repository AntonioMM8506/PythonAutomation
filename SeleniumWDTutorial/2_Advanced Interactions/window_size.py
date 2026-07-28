from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WindowSize():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        #driver.maximize_window()
        driver.get(baseURL)

        self.get_window_size(driver)
        time.sleep(2)
        driver.quit()
        # End of the test method

    def get_window_size(self, driver):
            # Get the current window size
            size = driver.get_window_size()
            width = size['width']
            height = size['height']
            print(f"Current window size: Width={width}, Height={height}")
        #End of the get_window_size method

ff = WindowSize()
ff.test()