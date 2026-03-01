# Write a class " calculator " capable of finding the
# suare,cube,squareroot of a number
import math
class calculator:
    @staticmethod
    def welcome():
        print("THANKS FOR USING ME")
    

    def __init__(self,number):
        self.number = number
        self.sqr = number*number
        self.cube = number* number*number
        self.sqrt = math.sqrt(number)

        print(f"The number is : {self.number}\n Square : {self.sqr}\n Cube : {self.cube}\n Square-root : {self.sqrt}")


num = calculator(36)        