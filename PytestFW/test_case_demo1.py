import pytest

# decorator to indicate that the method works as a fixture, so it can later be injected
@pytest.fixture()
def setUp():
    print("Before Each Test")
    # yield is used to return control to the test method, and after the test method is 
    # executed, the code after yield will be executed
    yield
    print("After Each Test")

def test_methodA(setUp):
    print("Executing test_methodA")

def test_methodB(setUp):
    print("Executing test_methodB")

# To run the tests in this file, you can use the following command in your terminal:
# pytest -v -s PytestFW/test_case_demo1.py

# To run a particular TC
# pytest -v -s PytestFW/test_case_demo1.py::test_methodA
# pytest -v -s PytestFW/test_case_demo1.py -k test_methodB