#WARLUS OPERATOR ":-" INTRODUCED IN PYTHON 3.8 
#Allows us to assign values to variable as part of an expression
if(n := len([1,2,3,4,5])) > 3:
    print(f"List is too long ({n} elements , expected <=3)")