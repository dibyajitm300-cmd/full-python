# write a program to draw the pattern
# *
# **
# ***
n=int(input("ENTER THE ROW: "))
for i in range(1,n+1):
    print("*"*i,end="")
    print("\n")