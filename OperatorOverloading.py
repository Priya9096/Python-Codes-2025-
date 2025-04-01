'''Magic Methods/dunder Methods:
The method which has suffix and prefix as double underscore such methods are called as Magic or
dunder Methods.
__init__()-->Called automatically while creating an object to initialize Instance variables.
__ str__()--> Called when we are trying to print object reference.
'''

class Student:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    def __truediv__(self,other):
        return self.name + other.name

s1 = Student("Pooja")
print(s1) #Pooja

s2 = Student("Akash")
print(s1) #Akash

print(s1 / s2)
