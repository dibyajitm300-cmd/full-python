# Create a class (2-D vector) and use it to create 
# another class representing a 3-D vector

class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)#Purpose: Access methods and properties of a parent class without explicitly naming it.
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")



D2 = TwoDVector(1,2)
D2.show()
D3 = ThreeDVector(1,2,3)
D3.show()
