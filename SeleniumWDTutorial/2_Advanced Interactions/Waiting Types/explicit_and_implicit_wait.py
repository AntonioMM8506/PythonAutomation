from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Explicit Wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Explicit Wait: Waits for a specific condition to occur before proceeding further in the code.
# Implicit Wait: Sets a default wait time for the entire duration of the WebDriver session

class ImplicitExplicitWait():
    def test(self):
        baseURL = "https://www.letskodeit.com/login"
        driver = webdriver.Chrome()
        driver.get(baseURL)

        # Implicit Wait
        driver.implicitly_wait(10)

        emailInput = driver.find_element(By.ID, "email")
        passwordInput = driver.find_element(By.ID, "login-password")

        emailInput.send_keys("test@email.com")
        passwordInput.send_keys("abcabc")

        time.sleep(3)

        # Explicit Wait
        wait = WebDriverWait(driver, 10)
        loginButton = wait.until(EC.element_to_be_clickable((By.ID, "login")))
        loginButton.click()

        # Wait until the URL changes to the expected URL after login
        wait.until(EC.url_to_be("https://www.letskodeit.com/"))
        # Wait until the header element is present and the text "My Courses" is visible
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#header5  div  nav")))
        # Wait until the text "My Courses" is present in the specified element
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".enrolled-courses .dynamic-heading"), "My Courses"))
        
        _course = "//*[@id='course-list']//*[contains(text(), '{0}')]"
        _courseLocator = _course.format("Java Step By Step For Testers")
        courseElement = wait.until(EC.element_to_be_clickable((By.XPATH, _courseLocator)))
        courseElement.click()

        driver.quit()

cc = ImplicitExplicitWait()
cc.test()