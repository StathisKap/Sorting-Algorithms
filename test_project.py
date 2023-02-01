import pytest
from project import generate_numbers

def test_generate_numbers():
    assert len(generate_numbers(100)) == 100
    with pytest.raises(SystemExit):
        generate_numbers(-100)
