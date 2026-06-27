from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class GetText():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, "opentab")

        # text method is used to retrieve the visible text of a web element. It returns a string representing the text 
        # content of the element, which can be useful for verification or logging purposes.
        tabText = openTabElement.text

        print("Text of the open tab element: " + tabText)
        time.sleep(2)


gt = GetText()
gt.test()