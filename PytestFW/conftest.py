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
def oneTimesetUp():
    print("Running one time setup")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("Running one time teardown")