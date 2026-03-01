from typing import List,Tuple,Dict,Union

#List of integers
numbers:List[int] = [1,2,3,4,5]

#Tuple of a string and an integer
person : Tuple[str,int] = ("Dibya",21)

#Dictionary with string as key and integer as values
score:Dict[str,int] = {"Dibya":21,"Bhabani":22}


#Union type for variable that can hold multiple types
idntfr:Union[int,str] = "ID34SB0043"
idntfr = 12345#Also valid


#Here we explicitly declare "n" as integer
n : int = 5
#Here we explicitly declare "name" as string
name : str = "Dibya"

#Here we explicitely declare a futeger nction named"sum"
# which will take 2 number as inand return a value of integer type
def sum(a:int,b:int) -> int:
    return a+b