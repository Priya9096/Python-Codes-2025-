class Demo1:
    def disp1(self):
        print('Inside disp1')
class Demo2:
    def disp2(self):
        print('Inside disp2')
class Demo3(Demo1, Demo2):
    def disp3(self):
        print('Inside disp3')

d3 = Demo3()
d3.disp3()
d3.disp2()
d3.disp1()