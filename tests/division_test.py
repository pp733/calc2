"""Testing Multiplication"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for addition"""
    #Arrange
    mynumbers = (2.0,2.0)
    division = Division(mynumbers)
    #Act
    #Assert
    assert division.get_result() == 1.0
