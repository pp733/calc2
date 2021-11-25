""" This is the increment function"""
#First import the addition namespace

from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division
from calc.history.calculations import Calculations

class Calculator:
    """ This is the Calculator class"""
    @staticmethod
    def add_number(*args):
        """ adds a list of numbers """
        calculation = Addition(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
    @staticmethod
    def subtract_number(*args):
        """ subtract a list of numbers from result """
        calculation = Subtraction(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def multiply_number(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()

    @staticmethod
    def division_number(*args):
        """ divides number from result"""
        calculation = Division(args)
        Calculations.add_calculation(calculation)
        return calculation.get_result()
