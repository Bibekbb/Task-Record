print("Hello World!!!")

import math

class SquareRootCalculator:
    def __init__(self, number):
        self.number = number
    
    def calculate(self):
        if self.number < 0:
            raise ValueError("Cannot calculate the square root of a negative number.")
        return math.sqrt(self.number)

# Example usage
try:
    num = float(input("Enter a number: "))
    calculator = SquareRootCalculator(num)
    result = calculator.calculate()
    print(f"The square root of {num} is {result}")
except ValueError as e:
    print(e)
