from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
from datetime import datetime
import random
import time

class Screenshots():

    def test(self):
        baseURL = "https://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        wait = WebDriverWait(driver, 15)

        flights_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//*[@role='tab' and normalize-space()='Flights']"))
        )
        flights_tab.click()

        dates_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@aria-label, 'Dates')]"))
        )
        dates_button.click()

        wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@role='dialog']")))

        day_to_select = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//*[@role='button' and normalize-space()='{random.randint(1, 28)}']"))
        )
        day_to_select.click()

        self.take_screenshot(driver, "my_screenshot")
    
        time.sleep(2)
        driver.quit()
        # End of the test method

    def take_screenshot(self, driver, filename):
            # Take a screenshot of the current state of the page
            # It is saved in the same directory as this script with a timestamp in the filename
        timestamp = datetime.now().strftime("%d%m%Y_%H%M")
        screenshot_path = Path(__file__).with_name(f"{filename}_{timestamp}.png")
        try:
            driver.save_screenshot(str(screenshot_path))
            print(f"Screenshot saved at: {screenshot_path}")
        except Exception as e:
            print(f"Error occurred while saving screenshot: {e}")
        #End of the take_screenshot method

ff = Screenshots()
ff.test()