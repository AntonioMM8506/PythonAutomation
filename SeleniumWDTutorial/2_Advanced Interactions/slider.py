from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Slider():

    def test(self):
        baseURL = "https://jqueryui.com/slider/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(5)

        driver.switch_to.frame(0)

        driver.find_element(By.ID, "slider")

        max_value = driver.execute_script("return $('#slider').slider('option', 'max');")
        current_value = driver.execute_script("return $('#slider').slider('value');")

        print(f"Current value: {current_value}")
        print(f"Max value: {max_value}")

        try:
            driver.execute_script("$('#slider').slider('value', $('#slider').slider('option', 'max'));")

            # Another way to move the slider to max value by using ActionChains
            # slider = driver.find_element(By.ID, "slider")
            # webdriver.ActionChains(driver).move_to_element(slider).click_and_hold().move_by_offset(100, 0).release().perform()
            
            print("Slider moved to max successfully.")
        except Exception as e:
            print(f"Error occurred while moving slider to max: {e}")

        time.sleep(2)
        driver.quit()


sl = Slider()
sl.test()