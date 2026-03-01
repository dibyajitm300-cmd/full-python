# Write a program to find out wheather a studeent has passed or failed if it requires total of 40% and at least 33% in each subject as pass
# Assume 3 subject and take marks from the useer
#Subject mark enterd by user
sub1=int (input("ENTER SUB1 MARKS: "))
sub2=int (input("ENTER SUB2 MARKS: "))
sub3=int (input("ENTER SUB3 MARKS: "))
total=(100*(sub1 + sub2 + sub3))/300
Tmark=300
if(total >= 40 and sub1>33 and sub2>33 and sub3>33 ):
    print("You are passed",total)
else:
    print("You are failed",total)