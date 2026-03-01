#Write a program to generate a multipliacation table from 2 to 20 and write into a the 
# different files.place these files in a folder a 13 year old
# for i in range(2,21):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i*j}")
def generateTable(n):
    table = ""
    for i in range(1,11):
        table = table + f"{n} X {i} = {n*i} \n"


    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)


for i in range(2,21):
    generateTable(i)