class Employee:
    a=100

    @classmethod#If user wants not to change the variable value through object change
    def show(cls):
        print(f"he class attrributr of a is {cls.a}")


e = Employee()
e.a=1997868
e.show()#show the class atribute insted of showing the object attribute
