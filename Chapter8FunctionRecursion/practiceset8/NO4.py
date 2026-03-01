# Write a recursive function to calculate the sum of 1st n number
def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)
n=int(input("Entere the number: "))
res = sum(n)
print(res)