from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WorkingWithIframes():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        # Switch to the iframe using its ID
        element = driver.find_element(By.ID, "courses-iframe")
        self.switch_to_iframe_by_id(driver, element)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

        # Perform actions inside the iframe (e.g., print the title)
        print("Inside iframe title:", driver.title)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # Scroll down inside the iframe
        time.sleep(2)  

        # Switch back to the default content
        driver.switch_to.default_content()
        print("Switched back to default content.")
        driver.execute_script("window.scrollTo(0, 0);") # Scroll to the top of the main page
        time.sleep(2)  

        driver.quit()

    # Switch to the iframe using its ID
    def switch_to_iframe_by_id(self, driver, iframe_id):
        try:
            driver.switch_to.frame(iframe_id)
            print(f"Switched to iframe with ID '{iframe_id}' successfully.")
        except Exception as e:
            print(f"Error occurred while switching to iframe: {e}")

iwf = WorkingWithIframes()
iwf.test()