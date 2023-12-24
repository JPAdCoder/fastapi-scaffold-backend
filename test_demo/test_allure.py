import pytest


def test_success():
    """
    this test_demo succeeds
    """
    assert True


def test_failure():
    """
    this test_demo fails
    """
    assert False


def test_skip():
    """
    this test_demo is skipped
    """
    pytest.skip('for a reason! Miss it')


def test_broken():
    raise Exception('oh, just broken')

