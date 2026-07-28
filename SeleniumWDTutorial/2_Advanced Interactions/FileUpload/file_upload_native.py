from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import time

class NativeFileUpload():
    def test(self):
        baseURL = "https://www.plupload.com/examples/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        upload_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#uploader input[type='file']"))
        )
        upload_input.send_keys(str(Path(__file__).parent / "tester.png"))

        time.sleep(2)
        driver.quit()


ff = NativeFileUpload()
ff.test()