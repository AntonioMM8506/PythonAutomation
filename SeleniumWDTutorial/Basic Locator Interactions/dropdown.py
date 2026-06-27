from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select 
import time

class DropDown():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        dropdown_element = driver.find_element(By.ID, "carselect")
        
        # Select class is used to interact with dropdown elements in Selenium. It provides methods to select options 
        # from a dropdown menu based on different criteria such as index, value, or visible text. The Select class is 
        # part of the selenium.webdriver.support.select module and is specifically designed for handling <select> HTML elements.
        # In this code, we create an instance of the Select class by passing the dropdown_element
        sel = Select(dropdown_element)

        sel.select_by_value("benz")
        time.sleep(2)

        sel.select_by_value("honda") 
        time.sleep(2)
        
        sel.select_by_visible_text("BMW")
        time.sleep(2)

ch = DropDown()
ch.test()