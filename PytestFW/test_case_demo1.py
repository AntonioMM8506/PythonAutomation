import pytest

# decorator to indicate that the method works as a fixture, so it can later be injected
@pytest.fixture
def setUp():
    print("Before Each Test")

def test_methodA(setUp):
    print("Executing test_methodA")

def test_methodB(setUp):
    print("Executing test_methodB")

# To run the tests in this file, you can use the following command in your terminal:
# pytest -v -s PytestFW/test_case_demo1.py