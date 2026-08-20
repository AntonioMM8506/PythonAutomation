from AutomationFramework.base.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CoursesPage(BasePage):

    path = "/courses"

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.url = f"{base_url.rstrip('/')}" + self.path

    _search_box = "search-courses"
    _course = "course"
    _all_courses = "course-list"
    _enroll_button = "button.btn-enroll"
    _cc_num = "#card-number iframe"
    _cc_exp = "#card-expiry iframe"
    _cc_cvv = "#card-cvc iframe"
    _buy_button = "button.zen-subscribe.sp-buy"
    _enroll_error_message = "li.card-no.cvc.expiry.text-danger"

    def searchCourse(self, courseName):
        self.type(self._search_box, "id", courseName)

    def selectCourse(self, fullCourseName):
        courses = self.driver.find_elements(By.CLASS_NAME, self._course)
        if not courses:
            courses = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/courses/']")
        for course in courses:
            if fullCourseName.lower() in course.text.lower():
                course.click()
                return True
        return False

    def enroll(self):
        self.click(self._enroll_button, "css")

    def _enterStripeField(self, iframeLocator, value):
        wait = WebDriverWait(self.driver, 10)
        try:
            iframe = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, iframeLocator)))
            self.driver.switch_to.frame(iframe)
            field = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "input:not(.StripeField--fake):not([name='hidden'])")
            ))
            field.send_keys(value)
        finally:
            self.driver.switch_to.default_content()

    def enterCardNum(self, num):
        self._enterStripeField(self._cc_num, num)

    def enterCardExp(self, exp):
        self._enterStripeField(self._cc_exp, exp)

    def enterCardCVV(self, cvv):
        self._enterStripeField(self._cc_cvv, cvv)

    def buy(self):
        self.click(self._buy_button, "css")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def verifyEnrollFailed(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self._enroll_error_message))
            )
            return True
        except Exception:
            return False

    def verifyEnrollMessageDisplayed(self):
        return self.verifyEnrollFailed()