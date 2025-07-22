class Person:
    def __init__(self,name,occu):
        print("hi every one nikunj is here")
        self.name = name
        self.occu = occu
    def info(self):
        print(f"{self.name} is a {self.occu}")
a = Person  ("hitansha", "lover")
b = Person("khushi", "lover")
a.info()
b.info()