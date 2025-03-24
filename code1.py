class Employee:
    name = 'Priya'
    age = 33

    def teach(self):
        print('Employee is Teaching')

e1 = Employee()
e2 = Employee()
print(e1.name)
print(e2.name)
e1.teach()
e2.teach()
'''
1.The Methods which are present inside the class are called as Instance(Object) Methods.
2.For Instance Methods self parameter is must.
'''