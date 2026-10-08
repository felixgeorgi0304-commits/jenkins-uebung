import pytest
from rechner import addiere, teile

def test_addiere():
    assert addiere(2, 3) == 5

def test_teile():
    assert teile(10, 2) == 5

def test_teile_durch_null():
    with pytest.raises(ValueError):
        teile(1, 0)
