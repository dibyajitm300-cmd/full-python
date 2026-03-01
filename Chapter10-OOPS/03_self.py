class Employee:#CLASS NAME IS THE "NOUN"
    language = "PYTHON"
    salary = 120000# THESE ARE THE ATTRIBUTES OR CALLED AS ADJECTIVE
    def getinfo(self):
        print(f"The language is {self.language}. \n The salary is {self.salary}")
    @staticmethod # Dont want to pass the whole object here
    def greet():
        print("GOOD MORNING")

obj = Employee()
obj.name="DIBYAJIT"
obj.language="java"
# print( obj.name,obj.salary,obj.language)    
obj.greet()
obj.getinfo()
# Employee.getinfo(obj)
