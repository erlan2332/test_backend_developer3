
from main import count_well_formed_parenthesis

def test_base_cases():
    assert count_well_formed_parenthesis(1) == 1
    assert count_well_formed_parenthesis(2) == 2
    assert count_well_formed_parenthesis(3) == 5

def test_known_values():
    assert count_well_formed_parenthesis(4) == 14
    assert count_well_formed_parenthesis(5) == 42
    assert count_well_formed_parenthesis(15) == 9694845