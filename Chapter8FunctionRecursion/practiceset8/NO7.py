# a program to print multiplication table of a given number
def multiTable(n):
    for i in range(1,n+1):
        print(f"{n}X{i} = {n*i}")

multiTable(5)    