from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class DragAndDrop():

    def test(self):
        baseURL = "https://jqueryui.com/droppable/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        source_element = driver.find_element(By.ID, "draggable")
        target_element = driver.find_element(By.ID, "droppable")

        try:
            # Perform the drag and drop action
            webdriver.ActionChains(driver).drag_and_drop(source_element, target_element).perform()

            # Another way to perform drag and drop action
            #webdriver.ActionChains(driver).click_and_hold(source_element).move_to_element(target_element).release().perform()
            print("Drag and drop action performed successfully.")
        except Exception as e:
            print(f"Error occurred while performing drag and drop action: {e}")
        time.sleep(2)

        driver.quit()

ff = DragAndDrop()
ff.test()
        