import pytest

@pytest.mark.run(order=2)
def test_methodA(setUp, oneTimesetUp):
    print("Executing test_methodA")

@pytest.mark.run(order=3)
def test_methodB(setUp, oneTimesetUp):
    print("Executing test_methodB")

@pytest.mark.run(order=5)
def test_methodC(setUp, oneTimesetUp):
    print("Executing test_methodC")

@pytest.mark.run(order=4)
def test_methodD(setUp, oneTimesetUp):
    print("Executing test_methodD")

@pytest.mark.run(order=6)
def test_methodE(setUp, oneTimesetUp):
    print("Executing test_methodE")

@pytest.mark.run(order=1)
def test_methodF(setUp, oneTimesetUp):
    print("Executing test_methodF")