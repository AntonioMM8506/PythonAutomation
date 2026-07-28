from pathlib import Path
import sys


def _ensure_wrappers_on_path() -> None:
    current_path = Path(__file__).resolve()
    for base_dir in [current_path.parent, *current_path.parents]:
        candidate_dir = base_dir / "Basic Locator Interactions" / "wrappers"
        if (candidate_dir / "handy_wrappers.py").exists():
            sys.path.insert(0, str(base_dir / "Basic Locator Interactions"))
            return

    raise ImportError(
        "Could not locate the 'wrappers' package. "
        "Expected to find 'Basic Locator Interactions/wrappers/handy_wrappers.py'."
    )


_ensure_wrappers_on_path()
from wrappers.handy_wrappers import HandyWrappers  # type: ignore[import]

from traceback import print_stack
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class ExplicitWaitType():
    def __init__(self, driver):
        self.driver = driver
        self.hw = HandyWrappers(driver)

    # This method is used to wait for an element to be clickable on the web page.
    # It takes the following parameters:
    # locator: The locator of the element to wait for.
    # locator_type: The type of locator (default is "id").
    # timeout: The maximum time to wait for the element to be clickable (default is 10 seconds).
    # poll_frequency: The frequency at which to check for the element's presence (default is 0.5 seconds).
    # The method returns the element if it becomes clickable within the specified timeout, or None if it does not.
    def wait_for_element(self, locator, locator_type="id", timeout=10, poll_frequency=0.5):
        element = None
        self.driver.implicitly_wait(0)  # Disable implicit wait for this method
        try:
            by_type = self.hw.get_by_type(locator_type)
            print("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            print("Element appeared on the web page")
        except:
            print("Element not appeared on the web page")
            print_stack()
            self.driver.implicitly_wait(10)  # Re-enable implicit wait after the method
        return element