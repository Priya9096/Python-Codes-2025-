class Add:
    def calculate(self,a,b):
        print(a+b)
class Mul:
    def calculate(self,a,b):
        print(a * b)
class Div:
    def calculate(self,a,b):
        print(a / b)

def permit(ref):
    ref.calculate(10,20)
    
permit(Add())
permit(Mul())
permit(Div())