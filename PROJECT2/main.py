import random
n = random.randint(1,100)#Choosen by the System
a = -1
guesses = 0
while(a != n):
    
    a = int(input("Guess a number : "))#Choosen by the user
    if(a > n):
        print(" Opps!!! Enter a Lower no please:-  ")
        guesses = guesses + 1
    elif(a < n):
        print("Opps!!! Enter a Higher no please:-  ")
        guesses = guesses + 1

print(f"You have guessed the number {n} correctly in {guesses} attempt")
