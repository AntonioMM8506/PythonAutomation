import pytest

# decorator to indicate that the method works as a fixture, so it can later be injected
@pytest.fixture()
def setUp():
    print("Before Each Test")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("After Each Test")

def test_methodA(setUp, oneTimesetUp):
    print("Executing test_methodA")

def test_methodB(setUp, oneTimesetUp):
    print("Executing test_methodB")