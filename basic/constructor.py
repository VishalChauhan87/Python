class Employee:
    language="py"
    salary=12000

    def __init__(self): #it no need to call it automatically called. it is also called dunder method.
        print("I am craeting a object.")


    def getinfo(self):
        print(f"The language is {self.language} .The salary is {self.salary}")

harry=Employee()
harry.language="java"
print(harry.salary,harry.language)
harry.getinfo()
