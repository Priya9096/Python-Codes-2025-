class Demo1:
    def __init__(self):
        self.x = 100
        super().__init__()
class Demo2:
    def __init__(self):
        self.x = 200
        super().__init__()
class Demo3(Demo1,Demo2):
    pass
d3 = Demo3()
print(d3.x) # 200 