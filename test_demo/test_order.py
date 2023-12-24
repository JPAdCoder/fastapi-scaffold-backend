import pytest


@pytest.mark.run(order=2)
def test_order1():
    print("first test_demo")
    assert True


@pytest.mark.slow(order=1)
def test_order2():
    print("second test_demo")
    assert True


