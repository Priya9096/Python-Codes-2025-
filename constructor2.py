class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id

    def learn(self):
        print(self.name,'is Learning')

    def play(self):
        print(self.name,'is Playing')

    def displayInfo(self):
        print('Student Details: ')
        print('Student Name is:',self.name)
        print('Student ID is:',self.id)

#Creating Objects:
s1 = Student('AK',101)
s2 = Student('PK',102)

#Access Methods for s1:
s1.learn()
s1.play()
s1.displayInfo()

#Access Methods for s2:
s2.play()
s2.displayInfo()