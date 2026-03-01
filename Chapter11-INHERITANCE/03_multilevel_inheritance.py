class Employee:#parent
    a=1
class Programmer(Employee):#child
    b=2
class Manager(Programmer):#grand child
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
