#THE PROGRAM TO READ THE TEXT FROM A GIVEN FILE "poem.txt" and find out wheather it contain thr word "twinkle"
with open("poem.txt","r") as f:
    content = f.read()
    if("twinkle" in content):
        print("twinkle is present in the content")
    else:
        print("not present")    