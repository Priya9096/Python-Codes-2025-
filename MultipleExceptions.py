def process(a,b):
    print(a/b)
try:
    process(10,0) 
except ZeroDivisionError:
    print('ZeroDivision Error occurred and Handled')
except NameError:
    print('Name Error occurred and Handled')
except TypeError:
    print('Type Error occurred and Handled')
except:
    print('Some Execption occurred and Handled')


print("Next Taks")