"""This is our calculation base class / Abstract Class"""

#This is the main calculation class
class Calculation:

    # Constructor and it is the first function called when an object of the class is instantiated
    def __init__(self, value_a, value_b):

        # Constructor
        self.value_a = value_a
        self.value_b = value_b

    # Class Factory Method
    @classmethod
    #This is the method
    def create(cls, value_a, value_b):
        # Creating the class method
        return cls(value_a, value_b)
