class Employee:
    company = "ITC"
    name = "DIBYAJIT"
    salary = 120000
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")


class coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all language the best is {self.language}")

class Programmer(Employee,coder):#Can inherit the functions of Employee and Coder class
    company = "ITC INFOTECH"
    language  = "JAVA-SCRIPT"
    def show_language (self):
        print(f"The name is {self.name} and he is good with {self.language} language")


# a =Employee()
b = Programmer()

b.show()
b.printLanguage()
b.show_language()
