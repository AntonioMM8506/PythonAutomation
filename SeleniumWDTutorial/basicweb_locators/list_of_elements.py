from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ElementList():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementListByTagName = driver.find_elements(By.TAG_NAME, "input")
        print("Size of the element list by tag name: " + str(len(elementListByTagName)))

        elementListByClassName = driver.find_elements(By.CLASS_NAME, "inputs")
        print("Size of the element list by class name: " + str(len(elementListByClassName)))

        radio_buttons = driver.find_elements(By.CSS_SELECTOR, "#radio-btn-example input[type='radio']")
        print("Size of the radio button list by CSS selector: " + str(len(radio_buttons)))

        checkboxes = driver.find_elements(By.CSS_SELECTOR, "#checkbox-example-div input[type='checkbox']")
        print("Size of the checkbox list by CSS selector: " + str(len(checkboxes)))

        for radio_button in radio_buttons:
            radio_button.click()
            time.sleep(1)

        for checkbox in checkboxes:
            checkbox.click()
            time.sleep(1)

ff = ElementList()
ff.test()