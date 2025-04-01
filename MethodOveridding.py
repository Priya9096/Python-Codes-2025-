class Parent:
    def cook(self):
        print("Cooking Biryani")
    def learn(self):
        print("Learning Maths")
        
class Child(Parent):
    def play(self):
        print('Playing Cricket')
    def learn(self):
        print("Learning Python")
c = Child()
c.cook()

'''
The Method which is derived from parent class and used as it is in child class, we call it as 
Inherited Method.

The Method which is only available for child class and not for parent class, such methods are
called as Specialized Methods.

The Methods which are derived from parent class and Modified into child class as per
child class requriment , such methods are called as Overidden Methods.
'''