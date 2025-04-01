class GreatGrandParent:
    def cook(self):
        print('GreatGrandParent cooks ABC')
        
class GrandParent(GreatGrandParent):
    def cook(self):
        print('GrandParent cooks Biryani')

class Parent(GrandParent):
    def cook(self):
        print('Parent cooks Pulao')

class Child(Parent):
    def cook(self):
        print('Child Cooks Maggie')
        super().cook() #Parent cooks Pulao
        super(Parent,self).cook() #GrandParent cooks Biryani
        super(GrandParent,self).cook() #GreatGrandParent cooks ABC

c = Child()
c.cook()