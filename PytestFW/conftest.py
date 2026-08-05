import pytest

# decorator to indicate that the method works as a fixture, so it can later be injected
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("Running method level tearDown")


# scope="module" means that the fixture will be executed only once for the entire 
# module, not before each test method. This is useful for setup that only needs to 
# be done once.
@pytest.fixture(scope="module")
def oneTimesetUp(browser, osType):
    print("Running one time setup")
    
    if browser == "chrome":
        print("Launching chrome browser")
    elif browser == "firefox":
        print("Launching firefox browser")
    else:
        print("Browser not supported")

    print("Running tests on OS:", osType)

    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("Running one time teardown")


# scope Class means that the fixture will be executed only once for the entire class, 
# not before each test method. This is useful for setup that only needs to be done once.
@pytest.fixture(scope="class")
def oneTimeClassSetUp(request, browser):
    print("Running one time setup")
    
    if browser == "chrome":
        value = 10
        print("Launching chrome browser")
    elif browser == "firefox":
        value = 15
        print("Launching firefox browser")
    else:
        value = 20
        print("Browser not supported")

    print("Running tests on OS:", osType)

    # request.cls is used to access the class that is using this fixture. This allows 
    # us to set attributes on the class that can be used in the test methods. In this 
    # case, we are setting the value attribute on the class to the value determined by 
    # the browser type.
    if request.cls is not None:
        request.cls.value = value

    yield
    print("Running one time teardown")


# This function is used to add command line options to pytest. In this case, it adds a
# "--browser" option that allows the user to specify which browser to use for testing.
# The default value is "chrome", but the user can specify "firefox" or other browsers as needed.
# The help argument provides a description of the option for the user.
# The parser.addoption method is used to define the option, and the action="store" argument
# indicates that the value provided by the user will be stored and can be accessed later in the tests.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome OR firefox")
    parser.addoption("--osType", action="store", default="windows", help="Type in OS name e.g. windows OR mac")


# The following two functions are used to retrieve the values of the command line options added above.
# The browser function retrieves the value of the "--browser" option, and the osType function retrieves the value of the 
#  "--osType" option. These functions can be used in test methods to determine which browser and operating system to use for testing.
# request is a built-in pytest fixture that provides access to the test context, including command line options and other test-related 
# information. The request.config.getoption method is used to retrieve the value of the specified command line option.
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# session scope means that the fixture will be executed only once for the entire test session, not before each test method.
@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
