from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Controller, Key
from pathlib import Path
import time

class SystemExplorerFileUpload():
    def test(self):
        baseURL = "https://www.plupload.com/examples/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)

        upload_button = driver.find_element(By.ID, "uploader_browse")
        upload_button.click()

        time.sleep(2)
        keyboard = Controller()
        keyboard.type(str(Path(__file__).parent / "test_file.txt"))
        keyboard.press(Key.enter)

        time.sleep(5)
        driver.quit()

ff = SystemExplorerFileUpload()
ff.test()