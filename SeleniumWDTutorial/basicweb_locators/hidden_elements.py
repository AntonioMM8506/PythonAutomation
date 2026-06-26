from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Hidden():
    def test(self):
        driver = webdriver.Chrome()
        driver.get("https://www.letskodeit.com/practice")
        driver.implicitly_wait(2)

        textbox = driver.find_element(By.ID, "displayed-text")

        print("Is the text box displayed? " + str(textbox.is_displayed()))

        driver.find_element(By.ID, "hide-textbox").click()
        time.sleep(2)

        print("Is the text box displayed? " + str(textbox.is_displayed()))

        driver.find_element(By.ID, "show-textbox").click()
        time.sleep(2)

        print("Is the text box displayed? " + str(textbox.is_displayed()))
        driver.quit()

ch = Hidden()
ch.test()