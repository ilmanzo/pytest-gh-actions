
from src import main


def test_myfunc():
    assert main.myfunc(2, 3) == 5


def test_failing():
    assert main.myfunc(4, 3) == 6
