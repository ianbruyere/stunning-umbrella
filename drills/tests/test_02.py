import pytest

import exercises.ex02_basic_data_types as ex


@pytest.fixture
def names():
    return [item for item in dir(ex) if not item.startswith("__")] 

def test_strings():
    assert isinstance(ex.string_4, str) is True

def test_integers(names):
    assert "not_integer" in names is True
    assert "not_integer_2" in names is True
    assert isinstance(ex.not_integer, int)
    assert isinstance(ex.not_integer_2, int)

def test_bools(names):
    assert "false" in names is True
    assert "true" in names is True
    assert "false_2" in names is True
    assert "true_2" in names is True
    assert ex.false == False
    assert ex.true == True
    assert isinstance(ex.false_2, bool) == True
    assert isinstance(ex.true_2, bool) == False
    
