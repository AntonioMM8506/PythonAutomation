from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class GetValueOfAttribute():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        openTabElement = driver.find_element(By.ID, "opentab")

        # get_attribute method is used to retrieve the value of a specified attribute of a web element. 
        # It takes the attribute name as an argument and returns the corresponding value as a string.
        tabHrefValue = openTabElement.get_attribute("href")

        print("Value of the href attribute of the open tab element: " + tabHrefValue)
        time.sleep(2)

        # The get_attribute method can be used to retrieve the value of any attribute of a web element, 
        # not just the href attribute.
        element = driver.find_element(By.ID, "bmwradio")
        elementValue = element.get_attribute("value")
        elementType = element.get_attribute("type")
        print("Value of the bmwradio element: " + elementValue)
        print("Type of the bmwradio element: " + elementType)

        driver.quit()

cc = GetValueOfAttribute()
cc.test()