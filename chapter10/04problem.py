from random import randint

class Train:

    def __init__(self,trainNo):
        self.trainNO = trainNo

    def book(self,fro ,to ):
        print(f"Ticket is booked in train{self.trainNO} from {fro} to {to}")

    def getstatus(self):
        print(f"The train no {self.trainNO} is running on time")

    def getfare(self,fro,to):
        print(f"Ticket fare in train no {self.trainNO} from {fro} to {to} is {randint(224,5556)}")


t=Train(123456)
t.book("RGP","BBSR")
t.getstatus()
t.getfare("RGP","BBSR")

