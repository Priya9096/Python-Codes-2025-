#Python does not support Method Overloading
def disp():
    print("Inside disp with 0 Parameters")
def disp(a):
    print("Inside disp with 1 parameter")
def disp(a,b):
    print("Inside disp with 2 parameters")
def disp(a,b,c):
    print("Inside disp with 3 parameters")

#disp() #Error: Missing 3 arguments
#disp(10) #Error: missing 2 required positional arguments
#disp(10,20)
disp(10,20,30)