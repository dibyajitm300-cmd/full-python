f=open("file.txt","r")
data = f.read()
print(data)
f.close()
#THE SAME CAN BE WRITTEN USINH "with" STATEMENT LIKE THIS:
with open("file.txt") as f:
    print(f.read())


#We don't have to explicitely close the file