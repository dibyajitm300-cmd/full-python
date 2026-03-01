# Write a program to copy a text file "this.txt"
with open ("log.txt","r") as s:
    content = s.read()


with open ("this.txt","w") as f:
    f.write(content)
        