a = int(input("Enter 1st Number: "))
b = int(input("Enter second number: "))

if(b==0):
    raise ZeroDivisionError ("Hey ur program is not meant to divide numbers by zero")
else:
    print(f"The division a/b is{a/b}")

    