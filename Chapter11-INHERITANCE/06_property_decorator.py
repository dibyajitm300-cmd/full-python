class Employee:
    a=100

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    
    @name.setter
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname =value.split(" ")[1]
       
e=Employee()

e.name="DIBYAJIT MOHANTY"
print(f"The 1s name of the emloyee is :{e.fname} \n  The last name of the employee is :{e.lname}")

e.show()