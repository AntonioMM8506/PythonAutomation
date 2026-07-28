from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class MouseHover():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        # Perform mouse hover action
        self.mouse_hover_action(driver)
        time.sleep(2)

        driver.quit()

    def mouse_hover_action(self, driver):
        try:
            # Locate the element to hover over
            element_to_hover = driver.find_element(By.ID, "mousehover")
            # Perform the mouse hover action
            webdriver.ActionChains(driver).move_to_element(element_to_hover).perform()
            print("Mouse hover action performed successfully.")
        except Exception as e:
            print(f"Error occurred while performing mouse hover action: {e}")

mh = MouseHover()
mh.test()