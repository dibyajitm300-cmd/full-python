# Wrie a program to display a/b where a and b are integers .
# if b =0 ,display infinite by handling the "ZeroDivisionError"
A = int (input("Enter the 1st  number: "))
B = int (input("Enter the 2nd number : "))

try:
    result = A/B
    print(result)

except ZeroDivisionError as e:
    print(f"infinite : {e}")    