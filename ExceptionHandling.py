def add(a,b):
    print("Start")
    print(a/b)

try:
    add(10,2)
except:
    print('Exception Occurred and Handled...!')
else:
    print("Ther is no Exception")
finally:
    print("End")

print('Other Tasks')