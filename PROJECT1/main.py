import random
'''
Docstring for PROJECT1.main
1 for SNAKE
-1 for WATER
0 for GUN
'''
computer = random.choice([1,-1,0])
youstr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
revDict = {1:"SNAKE",-1:"WATER",0:"GUN"}
you = youDict[youstr]
#by now we have 2 nymbers that is you and computer
#  
print(f"you choose {revDict[you]} \n computer chhose {revDict[computer]} ")

if(computer == you):
    print("MATCH DRAW")
# elif(computer==-1 and you==1):#-2
#     print("you win!")
# elif(computer==-1 and you==0):#-1
#     print("you lose!")
# elif(computer==1 and you==0):#1
#     print("you WIN!")
# elif(computer==1 and you==-1):#2
#     print("you LOSE!")
# elif(computer==0 and you==1):#-1
#     print("you lose!")
# elif(computer==0 and you==-1):#1
#     print("you win!")
# else:
#     print("SOMETHING WENT WRONG!!!!")    
elif((computer-you)== 1 or (computer - you)==-2):
    print("YOU WIN!!")
else:
    print("YOU LOSE!!")