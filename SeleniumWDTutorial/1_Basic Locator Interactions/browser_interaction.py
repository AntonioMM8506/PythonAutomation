from selenium import webdriver

class BrowserInteraction():
    def test(self):
        baseURL = "https://www.google.com/"
        driver = webdriver.Chrome()

        # get method is used to navigate to a specified URL. It takes the URL as an argument 
        # and opens the web page in the browser.
        driver.get(baseURL)

        # maximize_window method is used to maximize the browser window to full screen. 
        # It ensures that the web page is displayed in its entirety and provides a better view of the elements on the page.
        driver.maximize_window()

        # implicit wait method is used to set a default wait time for the entire duration of the WebDriver session.
        driver.implicitly_wait(10)

        # refresh method is used to reload the current web page. It can be useful when you want to ensure that you are 
        # working with the latest version of the page or when you want to reset the state of the page.
        driver.refresh()

        # back method is used to navigate back to the previous page in the browser's history. It simulates the action of 
        # clicking the browser's back button.
        driver.get("https://www.letskodeit.com/")
        driver.back()
        driver.implicitly_wait(100)

        # forward method is used to navigate forward to the next page in the browser's history. It simulates the action 
        # of clicking the browser's forward button.
        driver.forward()
        driver.implicitly_wait(100)

        # get_title method is used to retrieve the title of the current web page. It returns a string representing 
        # the title of the page, which can be useful for verification or logging purposes.
        print("The title of the page is: " + driver.title)

        # get_current_url method is used to retrieve the current URL of the web page. It returns a string representing
        # the URL of the page, which can be useful for verification or logging purposes.
        print("The current URL of the page is: " + driver.current_url)

        # get_current_url method is used to retrieve the current URL of the web page. It returns a string representing
        # the URL of the page, which can be useful for verification or logging purposes.
        print("The current URL of the page is: " + driver.current_url)

        # get_page_source method is used to retrieve the HTML source code of the current web page. It returns a string representing
        # the entire HTML content of the page, which can be useful for debugging or analysis purposes.
        source = driver.page_source
        print("The page source is: " + source)

        # close method is used to close the current browser window. If there are multiple windows open, it will only 
        # close the active window.
        driver.close()

        # quit method is used to close all the browser windows opened by the WebDriver and ends the WebDriver session. 
        # It is a more comprehensive way to clean up resources and terminate the browser session.
        driver.quit()

my_test = BrowserInteraction()
my_test.test()