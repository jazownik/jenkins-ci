"""
From https://docs.pytest.org/en/latest/ example
"""


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def test_second_answer():
    assert inc(15) == 16
