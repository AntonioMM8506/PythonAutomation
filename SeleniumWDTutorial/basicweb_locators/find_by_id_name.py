from selenium import webdriver
from selenium.webdriver.common.by import By

class find_elements():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseURL)
        
        #implicit wait method is used to set a default wait time for the entire duration of the WebDriver session. 
        #It tells the WebDriver to wait for a certain amount of time when trying to find an element if it is not 
        # immediately available. This can help to avoid issues with elements that may take some time to load or 
        # become interactable.
        driver.implicitly_wait(10)

        elementById = driver.find_element(By.ID, "displayed-text")
        if elementById is not None:
            print("We found the element by ID")
    
        # name property is not unique, so it will return the first element with the specified name.
        # not the same as class name, which is used to identify elements based on their CSS class attribute.
        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print("We found the element by Name")

        elemmentByXpath = driver.find_element(By.XPATH, "//input[@id='displayed-text']")
        if elemmentByXpath is not None:
            print("We found the element by Xpath")

        elementByCSS = driver.find_element(By.CSS_SELECTOR, "#displayed-text")
        if elementByCSS is not None:
            print("We found the element by CSS Selector")

        # Only works with <a> elements
        elementByLinkText = driver.find_element(By.LINK_TEXT, "HOME")
        if elementByLinkText is not None:
            print("We found the element by Link Text")

        elementByPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")
        if elementByPartialLinkText is not None:
            print("We found the element by Partial Link Text")

        # does not support 2 classes, only 1 class name can be used to find the element
        # if there are multiple elements with the same class name, it will return the first element it finds.
        elementByClassName = driver.find_element(By.CLASS_NAME, "inputs")
        if elementByClassName is not None:  
            print("We found the element by Class Name")
            elementByClassName.send_keys("Testing")

        elementByTagName = driver.find_element(By.TAG_NAME, "h1")
        if elementByTagName is not None:
            print("We found the element by Tag Name: " + elementByTagName.text)

run_test = find_elements()
run_test.test()
