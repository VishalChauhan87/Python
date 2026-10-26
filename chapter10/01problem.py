class Programmer:
    Company="Microsoft"

    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("harry",120000,770017)
print(p.name,p.salary,p.pin,p.Company)
x=Programmer("vishal",120000,770017)
print(x.name,x.salary,x.pin,x.Company)