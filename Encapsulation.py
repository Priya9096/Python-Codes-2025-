class Person:
    def __init__(self,name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self, newage):
        self.__age = newage

p1 = Person("Alice",33)
print(p1.name)
#print(p1.__age) Error
print(p1.get_age()) # 33
p1.set_age(55)
print(p1.get_age()) # 55
