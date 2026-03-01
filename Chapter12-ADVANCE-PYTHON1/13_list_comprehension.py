from typing import List

mylist :List[int] = [1,2,3,4,5,6,7,8,9]
# squaredList = []

# for item in mylist:
#     squaredList.append(item*item)
squaredList = [i*i for i in mylist]
print(squaredList)    