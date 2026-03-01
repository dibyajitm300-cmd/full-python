# using function o find the greatest of 3 number
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c
    

num1 = int(input("Enter the 1st nummmber: "))
num2 = int(input("Enter the 1st nummmber: "))    
num3 = int(input("Enter the 1st nummmber: "))        
grt = greatest(num1,num2,num3)
print(grt)