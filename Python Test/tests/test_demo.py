from app.demo import add


def test_add():
    assert add(10, 20) == 30


def test_sub():
    assert sub(10, 20) == -10
