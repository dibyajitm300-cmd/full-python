# Write a class train which has two menthods to book a ticket ,get status(no of seats)
#  and another is get fare information of train running under Indian railways
from random import randint
class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"The train is booked of train no : {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is running on time")


    def getFare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {randint(225,342)}")




t = Train(2345889)      
t.book("DHENKANAL","BHUBSNESWAR")
t.getStatus()
t.getFare("DHENKANAL","BHUBSNESWAR")  