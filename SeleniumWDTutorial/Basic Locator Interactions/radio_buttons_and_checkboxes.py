import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
import time

class RadioButtonsAndCheckBoxes():
    def test(self):
        baseURL = "https://www.letskodeit.com/practice"
        driver = webdriver.Firefox()
        driver.get(baseURL)
        
        #implicit wait method is used to set a default wait time for the entire duration of the WebDriver session. 
        #It tells the WebDriver to wait for a certain amount of time when trying to find an element if it is not 
        # immediately available. This can help to avoid issues with elements that may take some time to load or 
        # become interactable.
        driver.implicitly_wait(10)

        bmwRadioButton = driver.find_element(By.ID, "bmwradio")
        benzCheckBox = driver.find_element(By.ID, "benzcheck")
        hondaRadioButton = driver.find_element(By.ID, "hondaradio")
        hondaCheckBox = driver.find_element(By.ID, "hondacheck")

        bmwRadioButton.click()
        benzCheckBox.click()

        time.sleep(3)
        print("BMW Radio Button is selected? " + str(bmwRadioButton.is_selected()))
        print("Benz Check Box is selected? " + str(benzCheckBox.is_selected()))
        print("Honda Radio Button is selected? " + str(hondaRadioButton.is_selected()))
        print("Honda Check Box is selected? " + str(hondaCheckBox.is_selected()))

ff = RadioButtonsAndCheckBoxes()
ff.test()