
from main import count_well_formed_parenthesis

def test_performance(benchmark):
    result = benchmark(count_well_formed_parenthesis, 15)
    assert result == 9694845