class Employee:#parent
    def __init__(self):
        print("Constructer of Employee")
    a=1
class Programmer(Employee):#child
    def __init__(self):
        super().__init__()#call the super class constructer
        print("Constructer of Programmer")
    b=2
class Manager(Programmer):#grand child
    def __init__(self):#DUNDER METHOD RUN WHEN THE CLASS -OBJECT IS CREATED
        super().__init__()#call the super class constructer
        print("Constructer of Manager")
    c=3

  
# O = Employee()
# print(O.a)

# O = Programmer()
# print(O.a)
# print(O.b)

O = Manager()
print(O.a)
print(O.b)
print(O.c)
