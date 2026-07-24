from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HandlingJSPopup():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        # Click the button that triggers the JavaScript popup
        driver.find_element(By.ID, "alertbtn").click()
        time.sleep(2)

        # Handle the JavaScript alert
        self.handle_js_alert(driver)
        time.sleep(2)

        # Click the button that triggers the JavaScript confirmation popup
        driver.find_element(By.ID, "confirmbtn").click()
        time.sleep(2)

        # Handle the JavaScript confirmation
        self.handle_js_confirmation(driver)
        time.sleep(2)

        driver.quit()

    # Handle JavaScript alert
    def handle_js_alert(self, driver):
        try:
            alert = driver.switch_to.alert
            print("Alert text:", alert.text)
            alert.accept()  # Accept the alert
            print("Alert accepted.")
        except Exception as e:
            print(f"Error occurred while handling JS alert: {e}")

    # Handle JavaScript confirmation
    def handle_js_confirmation(self, driver):
        try:
            confirmation = driver.switch_to.alert
            print("Confirmation text:", confirmation.text)
            confirmation.dismiss()  # Dismiss the confirmation
            print("Confirmation dismissed.")
        except Exception as e:
            print(f"Error occurred while handling JS confirmation: {e}")

ff = HandlingJSPopup()
ff.test()