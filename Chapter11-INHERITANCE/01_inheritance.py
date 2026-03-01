class Employee:
    company = "ITC"
    name = "DIBYAJIT"
    salary = 120000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     name = "BHABANI"
#     salary = 130000
#     language = "JAVA-SCRIPT"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")


#     def show_language (self):
#         print(f"The name is {self.name} and he is good with {self.language} language")



#WE CAN WRITE THE ABOVE CODE BY USING THE FOLLOWING CODES

class Programmer(Employee):
    company = "ITC INFOTECH"
    language  = "JAVA-SCRIPT"
    def show_language (self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a =Employee()
b = Programmer()

print( f"\n { b.show_language()} ")
