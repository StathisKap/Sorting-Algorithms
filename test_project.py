import pytest
from project import generate_numbers, draw_columns, bubble_sort

def test_generate_numbers():
    assert len(generate_numbers(100)) == 100
    with pytest.raises(SystemExit):
        generate_numbers(-100)

def test_draw_columns():
        assert draw_columns([1,2]) == None

def test_bubble_sort():
    numbers = generate_numbers(10)
    bubble_sort(numbers)
    assert numbers == list(range(0,10))

def test_on_draw():
    pass

def test_on_key_press():
    pass
