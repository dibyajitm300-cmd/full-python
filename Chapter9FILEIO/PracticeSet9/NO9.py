#Write a program to find out wheather a file is identical and matches all thr content of another file
# import filecmp

# result = filecmp.cmp("log.txt", "this.txt", shallow=False)
# print(result)
def filecomparision(file1,file2):
    with open(file1,"r") as f,open (file2,"r") as g:
        if(f.read()==g.read()):
            print("MATCHED!!")
        else:
            print("NO MATCH FOUND")    


print(filecomparision("log.txt","this.txt"))