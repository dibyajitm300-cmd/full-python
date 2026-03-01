# A spam comment is defined as a text containing following keywords
#"Make a lot of money","Buy now","subscribe this","click this",
#Write a program to detect this
m1="Make a lot of money"
m2="Buy now"
m3="subscribe this"
m4="click this"
msg=input("Enter ur comment: ")
if((m1 in msg) or (m2 in msg) or (m3 in msg) or (m4 in msg)):
    print("SPAM ! DETECTED")
else:
    print("safe msg")