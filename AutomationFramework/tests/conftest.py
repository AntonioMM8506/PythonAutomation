import pytest
from selenium import webdriver
from AutomationFramework.base.selenium_driver import SeleniumDriver
from AutomationFramework.pages.login_page import LoginPage

@pytest.fixture()
def setUp():
    print("Running setup...")
    yield
    print("Running teardown...")

# This fixture captures screenshots on test failure
# Use case for taking a screenshot every time, regardless of pass/fail:
# if you want to record the UI state for debugging, visual validation, or comparing
# browser output across all tests, you can change the condition below to:
# if rep.when == "call":
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = getattr(item.instance, "driver", None)
        if driver is not None:
            try:
                SeleniumDriver(driver).screenShot(item.name)
            except Exception as e:
                print(f"Could not capture screenshot for failed test {item.name}: {e}")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome or firefox",
    )

@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    baseURL = "https://www.letskodeit.com/"

    driver = webdriver.Firefox() if browser == "firefox" else webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(baseURL)

    lp = LoginPage(driver, baseURL)
    lp.open(lp.url)
    lp.login("test@email.com", "abcabc")
    lp.verifyLoginSuccesful()

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.baseURL = baseURL

    yield driver
    driver.quit()