class Employee:
    language="py"
    salary=12000
    def getinfo(self):
        print(f"The language is {self.language} .The salary is {self.salary}")

harry=Employee()
harry.language="java"
print(harry.salary,harry.language)
harry.getinfo()
