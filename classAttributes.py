class Emp:
    college_name = 'SJBIT'
    def __init__(self, name):
        self.name = name

e1 = Emp('Akash')
e2 = Emp('Ankit')


# class level variables can be accessed using object reference or class Name:
print(e1.college_name)
print(e2.college_name)
print(Emp.college_name)

'''
class vs Instance Variables:

class level variables are such variables which are declared inside the class and outside any
method.
All objects for that class shares same copy copy of class variables.

Instance variables are such variables which are present inside objects.
For each object seperate copy of instace variables will be created.
'''