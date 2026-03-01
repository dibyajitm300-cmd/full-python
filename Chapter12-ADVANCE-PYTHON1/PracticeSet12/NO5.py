# Store the multiplication tables generated in problem 3 in a file named Tables.txt
from typing import List

number = int (input("Enter the number : "))

mulTable :List[int] = []

mulTable = [number * i for i in range(1,11)]
with open ("Table.txt","a")as f:
    f.write(f"{str(mulTable)} /n ")