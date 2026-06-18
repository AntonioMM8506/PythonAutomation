from selenium import webdriver
from selenium.webdriver.common.by import By

class find_by_id_name():
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

        elementByName = driver.find_element(By.NAME, "show-hide")
        if elementByName is not None:
            print("We found the element by Name")

run_test = find_by_id_name()
run_test.test()
