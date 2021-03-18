from calculator import *
import pytest
def test_function_add():
    result = function_add(1, 2)
    assert result == 3

# 减法
def test_function_sub():
    result = function_sub(1, 2)
    assert result == -1

# 乘法
def test_function_mul():
    result = function_mul(1, 2)
    assert result == 2

# 除法
def test_function_div():
    result = function_div(1, 2)
    assert result == 0.5

if __name__ == "__main__":
    pytest.main("-s test_calculator.py")