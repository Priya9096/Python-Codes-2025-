# string to int conversion:
'''
In Python while converting string to int , only when string is holding int value to int 
conversion is allowed.
'''
print(int('12')) # 12
# print(int('code')) #Error
# print(int('12.44')) #Error
# print(int('True')) #Error

#WAC to take 2 float numbers from user and display its addition.
num1 = float(input('Enter num1  :'))
num2 = float(input('Enter num2  :'))
print(num1, type(num1), num2 , type(num2))
print('Addition is:',round(num1 + num2,2))

print(round(123.567890987,3))
print('{:.3f}'.format(123.567890987))