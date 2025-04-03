'''The protected variables must be accessed inside the same class or inside child class.'''
class Demo1:
    def __init__(self):
        self._name = 'Ak' #Protected variable
    def disp1(self):
        print(self._name) #Accessing inside the same class

d1 = Demo1()
print(d1._name) #Accessing outside class is not allowed (Dev. should take care of this rule)
class Demo2(Demo1):
    def disp(self):
        print(self._name) #Accessing inside child class

d2 = Demo2()
