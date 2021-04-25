
import pytest
from keyword import iskeyword

import drills.exercises.ex01_assigning_objects as data

@pytest.fixture
def names():
    return [item for item in dir(data) if not item.startswith("__")]

def test_name_change(names):
    assert all(["change" not in name for name in names]) == True, "Ensure none of your variable names have 'change' in them"
    

