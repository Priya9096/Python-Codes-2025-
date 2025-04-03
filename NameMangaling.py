class Demo:
    def __init__(self):
        self.__x = 100
    def disp(self):
        print(self.__x) #100

d = Demo()
d.disp()
print("Accessing private variables outside the class:",d._Demo__x) 

'''
Name Mangling:
Is the process of giving new name to th private variables in format of: _ClassName__VariableName.

If we want to access private variables outside the class then use: _className__variableName
'''