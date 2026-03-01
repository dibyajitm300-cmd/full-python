# Repeat program 4 for a such words to be censored
words = ["Donkey","Bhai"]

with open ("file.txt","r") as f:
    content = f.read()

for word in words:
    content = content.replace(word,"#"*len(word))
with open ("file.txt","w") as f:
    content = f.write(content)