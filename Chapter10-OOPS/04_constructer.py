class Employee:#CLASS NAME IS THE "NOUN"
    language = "PYTHON"
    salary = 120000# THESE ARE THE ATTRIBUTES OR CALLED AS ADJECTIVE
        
    def __init__(self,name,salary,language):#THIS IS THE DUNDER METHOD  which is automatically called
                        # when an object is created
        print("Iam creating an object")
        self.name=name
        self.salary=salary
        self.language = language

    
    
    # def getinfo(self):
    #     print(f"The language is {self.language}. \n The salary is {self.salary}")
    @staticmethod # Dont want to pass the whole object here
    def greet():
        print("GOOD MORNING")

obj = Employee("DIBYA",1300000,"javascript")
# obj.name="DIBYAJIT"
# obj.language="java"
print( obj.name,obj.salary,obj.language)    
obj.greet()
# obj.getinfo()
# Employee.getinfo(obj)
# obj2 = Employee()
