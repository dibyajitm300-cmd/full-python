try:
    a = int(input("Hey !,Enter a number : "))
    


except Exception as e:
    print(e)

else:#If try block runs succesfully then else block run definately
    print("I am inside else")   
    print(a)     