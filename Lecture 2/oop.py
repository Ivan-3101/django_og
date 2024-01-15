class Person:
    def __init__(self,name,age,country):
        self.x = name
        self.y = age
        self.z = country

    def printName(self):
        print(f"Hello {self.x}")
        

p1 = Person("Ivan",19,"IND")
p2 = Person("Bruno",28,"POR")

print(p1.x)
# go into p1 and access its x value

p1.printName()