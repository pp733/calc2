"""This is the addition calculation that is being inherits the value A and value B from the calculation class"""

#This is called a namespace it is like files and folders the classes are files and the folders organise the classes
#It looks like a folder and file path but it is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#Thisis how you extend the Addition class with the calculation
class Subtraction(Calculation):
    """This addition class has one method to get the result of the calculation A and B come from the
    calculation parent class"""

    def getresult(self):
        #you need to use self to reference the data contained in the instance of the object. This is encapsulation
        return self.value_a - self.value_b
