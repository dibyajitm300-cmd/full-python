# Write a program to remove a given word from alist and strip it at the sane TimeoutErro
def rem(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n    
l = ["DIBYA","MADHUU","mohanty","aunty","bunty","ty"]
print(rem(l,"ty"))