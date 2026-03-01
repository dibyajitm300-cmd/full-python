# Write a program to mine a log file and find out the wheather it contains "python"
word = "DIVINE"

with open("log.txt") as f:
    content = f.read()


if( word in content):
    print("The python is available")
else:
    print("Word is not available")