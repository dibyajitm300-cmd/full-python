# Write a program to find wheather a given number is prime or not
num = int(input("Enter a number: "))
for i in range(2,int(num/2)):
    if(num%i==0):
        print("NOT PRIME")
        break
else:
    print("Prime")    