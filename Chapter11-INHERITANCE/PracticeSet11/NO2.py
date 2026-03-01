# Create a class 'pets' from a class 'Animal' and further create a class "Dog"
# from "Pets" Add a method "barl" to class "Dog"
class Animals:
    pass

class Pets(Animals):
    pass


class Dog(Pets):
     def bark(self):
         print("BOW BOW")


D = Dog()
D.bark()