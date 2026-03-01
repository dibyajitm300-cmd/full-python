# Write a program to find the maximum of the numbers in a list using the reduce function
from functools import reduce 

l = [1,2,3,4,55,50,25,65,89,67,100]

def greate(x,y):
    if(x>y):
        return x
    return y

print(reduce(greate,l))