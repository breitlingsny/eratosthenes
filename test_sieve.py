from sievetools import *
import pytest

def test_slow_interior():
    output = sieve_slow(10)
    expected = [2,3,5,7]
    
    assert output == expected

def test_slow_2():
    output = sieve_slow(2)
    expected = [2]
    
    assert output == expected

def test_slow_1():
    output = sieve_slow(1)
    expected = []
    
    assert output == expected

def test_slow_noninteger():
    with pytest.raises(TypeError):
        sieve_slow(3.14159)