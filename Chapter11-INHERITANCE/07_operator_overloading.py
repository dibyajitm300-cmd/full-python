class Number:
    def __init__(self,n):
        self.n=n

    def __add__(self,num):
        return self.n + num.n
    #it will add 




n = Number(1)
m = Number(3)

print(n + m) # add n.n + m.n