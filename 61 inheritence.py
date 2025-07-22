class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdetails(self):
        print(f"the name os employee: {self.id} is {self.name }")

class Programmer(Employee):
    def showlanguage(self):
        print("the defau language is c ")
e1 = Employee ("nikunj",69)
e1.showdetails()
e2 = Programmer("nikunj",847)
e2.showlanguage()
e2.showdetails()
