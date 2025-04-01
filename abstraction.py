from abc import ABC , abstractmethod

'''Rule: 1 We can create an Object for empty abstract class '''
class Animal1(ABC):
    pass
a1 = Animal1()

'''Rule: 2 If abstract class contains abstract method then object for that abstract class 
cannot be created and abstract method cannot be invoked.'''
class Animal2(ABC):
    @abstractmethod
    def eat(self):
        pass
# a2 = Animal1()

'''Rule: 3 If abstract class contains only concrete methods , then object can be created and
concrete method can be invoked.'''
class Animal3(ABC):
    def eat(self):
        print('Inside eat')
a3 = Animal3()
a3.eat()

'''Rule 4: If class is derived from abstract class and not given body for all abstract methods
in child class then child class objcet cannot be created.'''
class Animal4(ABC):
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Child(Animal4):
    def eat(self):
        print('Inside eat')
# c = Child() Not allowed