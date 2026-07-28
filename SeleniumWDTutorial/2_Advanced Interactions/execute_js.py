from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class JavaScriptExecution():

    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        element = driver.find_element(By.ID, "name")
        element.send_keys("Selenium WebDriver")
        self.execute_javascript(driver)
        time.sleep(2)
        driver.quit()
        # End of the test method

    def execute_javascript(self, driver):
            # Execute JavaScript to change the background color of the page
            # script variable contains the JavaScript code to be executed
            script = "document.body.style.backgroundColor = 'lightblue';"

            # Example of executing JavaScript to get the value of an element
            # script = driver.execute_script("return document.getElementById('name').value;")
            
            try:
                driver.execute_script(script)
                print("JavaScript executed successfully.")
            except Exception as e:
                print(f"Error occurred while executing JavaScript: {e}")
        #End of the execute_javascript method

ff = JavaScriptExecution()
ff.test()