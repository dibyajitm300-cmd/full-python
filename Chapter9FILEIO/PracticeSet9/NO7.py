# Write a program to find out the line number where python is present in que 6
word = "python"

with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if( word in lines):
        print(f"The python is available at line no : {lineno}")
        break
    lineno = lineno +1
else:
    print("Word is not available")