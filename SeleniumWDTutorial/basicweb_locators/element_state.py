from selenium import webdriver
from selenium.webdriver.common.by import By

class ElementState():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, "displayed-text")
        if elementById is not None:
            print("We found the element by ID")

        # is_displayed method is used to check if an element is visible on the web page. 
        # It returns a boolean value indicating whether the element is currently displayed or not.
        print("Is the element displayed? " + str(elementById.is_displayed()))

        # is_enabled method is used to check if an element is enabled and can be interacted with. 
        # It returns a boolean value indicating whether the element is currently enabled or not.
        print("Is the element enabled? " + str(elementById.is_enabled()))

        # is_selected method is used to check if an element, such as a checkbox or radio button, 
        # is currently selected or checked. It returns a boolean value indicating whether the element is selected or not.
        print("Is the element selected? " + str(elementById.is_selected()))

ff = ElementState()
ff.test()