from app.demo import *
import pytest


def test_add():
    assert add(10, 20) == 30


def test_sub():
    assert sub(10, 20) == -10


def test_mul():
    assert mul(10, 2) == 20


def test_div():
    assert div(10, 5) == 2

    # Case for exception
    with pytest.raises(ValueError):
        div(5, 0)
