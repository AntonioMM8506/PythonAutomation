import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    print("Running setup...")
    yield
    print("Running teardown...")

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

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.baseURL = baseURL

    yield driver
    driver.quit()