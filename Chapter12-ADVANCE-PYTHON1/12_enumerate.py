l = [1,2,3,4,5,6,7,8,9]

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index = index +1

#This can be simplified using enumerate function

for index,item in enumerate(l):
    print(f"The item number at index {index} is {item}")