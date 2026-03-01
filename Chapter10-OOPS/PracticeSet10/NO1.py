# Create a class "Programmer" for storing information of the 
# programmers working at microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,language,pin):
        
        self.name=name
        self.salary = salary
        self.language = language
        self.pin = pin
        print(f" company name = {self.company} \n The name of the Employee is {self.name} \n salary = {self.salary} \n language = {self.language} \n pin = {self.pin}")



programmer1 = Programmer("DIBYAJIT",1200000,"PYTHION",759001)

programmer2 = Programmer("BHABANI",1400000,"JAVASCROPT",759003)
        