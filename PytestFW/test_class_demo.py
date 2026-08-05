import pytest
from class_to_test import ClassToTest

# The @pytest.mark.usefixtures decorator is used to specify that the oneTimeClassSetUp 
# and setUp fixtures should be applied to all test methods in this class. This means 
# that the setup and teardown code defined in those fixtures will be executed before 
# and after each test method, respectively.
@pytest.mark.usefixtures("oneTimeClassSetUp", "setUp")
class TestClassDemo():

    # The @pytest.fixture(autouse=True) decorator is used to indicate that the setup_class 
    # method should be automatically executed before any test methods in this class. 
    # This is useful for setting up any necessary state or objects that will be 
    # used in the test methods.
    @pytest.fixture(autouse=True)
    def setup_class(self, oneTimeClassSetUp):
        print("Running setup_class")
        self.obj = ClassToTest(self.value) # self.value is set in the oneTimeClassSetUp fixture

    def test_add(self):
        result = self.obj.add(5, 3)
        assert result == 18, f"Expected 18 but got {result}"

    def test_subtract(self):
        result = self.obj.subtract(5, 3)
        assert result == -2, f"Expected -2 but got {result}"
