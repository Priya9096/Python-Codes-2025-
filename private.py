'''Private Variables must be accessed inside the same class.'''
class Demo1:
    def __init__(self):
        self.__name = 'Ak' #Private variable
    def disp1(self):
        print(self.__name) #Accessing inside the same class

d1 = Demo1()
#print(d1.__name) #Error

'''
public: When we want to access variables anywhere in the code.
protected: When we want to access variables inside the same class and inside child class.
private: When we want to access variables inside the same class.


public: a = 10
protected: _a = 10
private: __a = 10
'''