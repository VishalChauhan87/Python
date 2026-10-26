class Calculator:
    def __init__(self,n):
        self.n=n

    def Square(self):
        print(f"The square of the number is {self.n*self.n}")

    def Cube(self):
            print(f"The cube of the number is {self.n*self.n*self.n}")


    def Squareroot(self):
                print(f"The squareroot of the number is {self.n**1/2}")

    @staticmethod
    def hey():
          print("hey")
    
    

a=Calculator(5)

a.Square()
a.Cube()
a.Squareroot()
a.hey()
