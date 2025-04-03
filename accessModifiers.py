class Demo:
    def __init__(self):
        self.name = "Priya"
    def disp(self):
        print(self.name) #Accessing Public property inside the same class - Allowed
d1 = Demo()
print(d1.name) #Accessing Public property outside the class - Allowed

class Demo1(Demo):
    def disp(self):
        print(self.name) #Accessing Public property inside child class - Allowed
dm1 = Demo1()
dm1.disp()

class Code:
    def display(self):
        print(d1.name) #Accessing Public property inside Non-Child class - Allowed
c = Code()
c.display()