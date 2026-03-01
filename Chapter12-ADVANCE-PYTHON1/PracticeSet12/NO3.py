# WRITE A LIST COMPREHENSION TO PRINT A LIST WHICH CONTAINS THE MULTIPLIACATION TABLE OF A ENTERD NUMBER
from typing import List
number = int (input("Enter the number : "))

mulTable :List[int] = []

mulTable = [number * i for i in range(1,11)]
print(mulTable)