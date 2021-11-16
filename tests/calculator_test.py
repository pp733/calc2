#importing pprint
import pprint

#importing pytest
import pytest

#importing the main calculator class
from calculator.calculator import Calculator

#this is how you define a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()

def test_clear_history(clear_history):
    """Testing clear History"""
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(2, 2) == 0
    assert Calculator.subtract_number(3, 2) == 1
    assert Calculator.subtract_number(4, 2) == 2
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() == True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    """Testing history count"""
    assert Calculator.history_count() == 0
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(2, 2) == 0
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    """Testing to make sure it is getting the proper last results"""
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(2, 2) == 0
    assert Calculator.get_result_of_last_calculation_added_to_history() == 0

def test_get_first_calculation_result(clear_history):
    """Testing to make sure it is getting the proper first results"""
    assert Calculator.subtract_number(1, 2) == -1
    assert Calculator.subtract_number(2, 2) == 0
    assert Calculator.get_result_of_first_calculation_added_to_history() == -1

def test_calculator_add(clear_history):
    """testing calculator result is 0"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    assert Calculator.get_result_of_first_calculation_added_to_history() == 3


def test_calculator_subtract(clear_history):
    """testing calculator result is 0"""
    assert Calculator.subtract_number(1,2) == -1
    assert Calculator.subtract_number(2, 2) == 0
    assert Calculator.subtract_number(3, 2) == 1
    assert Calculator.subtract_number(4, 2) == 2
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 2
    assert Calculator.get_result_of_first_calculation_added_to_history() == -1

def test_calculator_multiply(clear_history):
    """testing calculator result is 0"""
    assert Calculator.multiply_number(1,2) == 2
    assert Calculator.multiply_number(2, 2) == 4
    assert Calculator.multiply_number(3, 2) == 6
    assert Calculator.multiply_number(4, 2) == 8
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 8
    assert Calculator.get_result_of_first_calculation_added_to_history() == 2

def test_calculator_divide(clear_history):
    """testing calculator result is 0"""
    assert Calculator.division_number(2,1) == 2
    assert Calculator.division_number(4, 1) == 4
    assert Calculator.division_number(5, 1) == 5
    assert Calculator.division_number(6, 1) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    assert Calculator.get_result_of_first_calculation_added_to_history() == 2
