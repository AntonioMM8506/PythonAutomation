import pytest

# decorator to indicate that the method works as a fixture, so it can later be injected
@pytest.fixture()
def setUp():
    print("Before Each Test")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("After Each Test")

# scope="module" means that the fixture will be executed only once for the entire 
# module, not before each test method. This is useful for setup that only needs to 
# be done once.
@pytest.fixture(scope="module")
def oneTimesetUp():
    print("Start One Time Setup")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("End One Time Setup")