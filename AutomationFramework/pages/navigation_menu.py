from selenium.webdriver.common.by import By
from AutomationFramework.base.basepage import BasePage


class NavigationMenu(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home_link_locator = (By.LINK_TEXT, "HOME")
    _courses_link_locator = (By.LINK_TEXT, "ALL COURSES")
    _practice_link_locator = (By.LINK_TEXT, "PRACTICE")
    _blog_link_locator = (By.LINK_TEXT, "BLOG")
    _interview_link_locator = (By.LINK_TEXT, "INTERVIEW")
    _support_link_locator = (By.LINK_TEXT, "SUPPORT")
    _login_link_locator = (By.LINK_TEXT, "Login")
    _user_menu_locator = (By.ID, "dropdownMenu1")
    _user_settings_locator = (By.XPATH, ".//*[@id='navbar']//span[text()='User Settings']")

    # Transaction methods
    def clickHome(self):
        self.click(self._home_link_locator[1], self._home_link_locator[0])

    def clickAllCourses(self):
        self.click(self._courses_link_locator[1], self._courses_link_locator[0])

    def clickPractice(self):
        self.click(self._practice_link_locator[1], self._practice_link_locator[0])

    def clickBlog(self):
        self.click(self._blog_link_locator[1], self._blog_link_locator[0])

    def clickInterview(self):
        self.click(self._interview_link_locator[1], self._interview_link_locator[0])

    def clickSupport(self):
        self.click(self._support_link_locator[1], self._support_link_locator[0])

    def clickLogin(self):
        self.click(self._login_link_locator[1], self._login_link_locator[0])

    def clickUserMenu(self):
        self.click(self._user_menu_locator[1], self._user_menu_locator[0])

    def clickUserSettings(self):
        self.click(self._user_settings_locator[1], self._user_settings_locator[0])
