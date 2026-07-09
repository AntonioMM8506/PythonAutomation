from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time


class CalendarSelection():
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

        print("Date selected successfully")
        time.sleep(2)
        driver.quit()


ff = CalendarSelection()
ff.test()