# Write a program to filter a list of number divisible by 5
l = [1,2,3,4,55,50,25,65,89,67,100]

def divis(n):
    if(n%5==0):
        return True
    return False


result = list(filter(divis,l))

print(result)