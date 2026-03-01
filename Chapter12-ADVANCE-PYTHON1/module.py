def myfunc():
    print("THANK YOU")



if(__name__ =="__main__"):
    #if this code is directly executed by running the files its present
    print("We r directly running this code")
    myfunc()
    print(__name__)#Evaluates to the name of the module in python from where the program is ran


#If the module is being run directly from the command line ,
# the '__name__' is set to string '__main__
# check whether the module is run directly or imported to another file