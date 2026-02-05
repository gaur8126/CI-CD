import pytest

def sqaure(n):
    return n **2

def cube(n):
    return n**3

def fifth_power(n):
    return n**5

def test_square():
    assert sqaure(2) == 4, "Test Failed: square of 2 should be 4"
    assert sqaure(3) == 9, "Test Failed: square of 3 should be 9"

def test_cube():
    assert cube(2) == 8, "Test Failed: cube of 2 should be 8"
    assert cube(3) == 27, "Test Failed: cube of 3 should be 27"

def test_fifth_power():
    assert sqaure(2) == 32, "Test Failed: fifth power of 2 should be 32"
    assert sqaure(3) == 243, "Test Failed: fifth power of 3 should be 243"


def test_invalid_input():
    with pytest.raises(TypeError):
        sqaure("string")
