from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ScrollElementIntoView():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        element = driver.find_element(By.ID, "mousehover")

        self.scroll_into_view(driver, element)
        time.sleep(2)

        self.scroll_into_view_with_offset(driver, element, 100)
        time.sleep(2)

        self.scroll_into_view_with_offset_and_delay(driver, element, 100, 2)
        time.sleep(2)

        self.scroll_down_by_offset(driver, 200)
        time.sleep(2)

        self.scroll_up_by_offset(driver, 200)
        time.sleep(2)

        self.scroll_to_bottom(driver)
        time.sleep(2)

        self.scroll_to_top(driver)
        time.sleep(2)

        self.scroll_native(driver, 100, 200)
        time.sleep(2)

        driver.quit()
        # End of the test method

    # Scroll the specified element into view using JavaScript
    def scroll_into_view(self, driver, element):
            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", element)
                print("Scrolled element into view successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling element into view: {e}")
        #End of the scroll_into_view method

    # Scroll the specified element into view with an offset using JavaScript
    def scroll_into_view_with_offset(self, driver, element, offset):
            try:
                driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, arguments[1]);", element, offset)
                print(f"Scrolled element into view with offset {offset} successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling element into view with offset: {e}")
        #End of the scroll_into_view_with_offset method

    # Scroll the specified element into view with an offset and delay using JavaScript
    def scroll_into_view_with_offset_and_delay(self, driver, element, offset, delay):
            try:
                driver.execute_script("arguments[0].scrollIntoView(true); window.scrollBy(0, arguments[1]);", element, offset)
                time.sleep(delay)
                print(f"Scrolled element into view with offset {offset} and delay {delay} seconds successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling element into view with offset and delay: {e}")
        #End of the scroll_into_view_with_offset_and_delay method

    # Scroll down the page by a specified offset using JavaScript
    def scroll_down_by_offset(self, driver, offset):
            try:
                driver.execute_script("window.scrollBy(0, arguments[0]);", offset)
                print(f"Scrolled down by offset {offset} successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling down by offset: {e}")
        #End of the scroll_down_by_offset method    

    # Scroll up the page by a specified offset using JavaScript
    def scroll_up_by_offset(self, driver, offset):
            try:
                driver.execute_script("window.scrollBy(0, -arguments[0]);", offset)
                print(f"Scrolled up by offset {offset} successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling up by offset: {e}")
        #End of the scroll_up_by_offset method

    # Scroll to the bottom of the page using JavaScript
    def scroll_to_bottom(self, driver):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                print("Scrolled to the bottom of the page successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling to the bottom of the page: {e}")
        #End of the scroll_to_bottom method
    
    # Scroll to the top of the page using JavaScript
    def scroll_to_top(self, driver):
            try:
                driver.execute_script("window.scrollTo(0, 0);")
                print("Scrolled to the top of the page successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling to the top of the page: {e}")
        #End of the scroll_to_top method
    
    # Scroll the page by native offsets using JavaScript
    def scroll_native(self, driver, x_offset, y_offset):
            try:
                driver.execute_script(f"window.scrollBy({x_offset}, {y_offset});")
                print(f"Scrolled by native offsets X: {x_offset}, Y: {y_offset} successfully.")
            except Exception as e:
                print(f"Error occurred while scrolling by native offsets: {e}")
        #End of the scroll_native method

ff = ScrollElementIntoView()
ff.test()