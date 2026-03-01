# Create a class "Employee" and add salary and increament properties to it
class Employee:
    def show(self):
        print(f"The salary is {self.salary}")
        print(f"The increament valu is {self.increament}")
    @property
    def salaryAfterIncreament(self):#This makes  behave like a variable, not a method.
        return (self.salary + self.increament)
    

    @salaryAfterIncreament.setter#- This allows you to assign a value to salaryAfterIncreament

    def salaryAfterIncreament(self,salary):#nstead of directly setting salary, it calculates how much increment is needed to reach that new salary.
        self.increament = salary - self.salary




e = Employee()
e.salary = 23400
e.increament = 10000
# e.show()
# print(e.salaryAfterIncreament)
e.salaryAfterIncreament = 500000
print(e.increament)
# Write a methof "salaryAfterIncreament" method with a @property decorator
# with a setter which changes the value of increament based on the salary
