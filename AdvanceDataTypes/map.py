li = [1,2,3,4]

def square(ele):
    return ele * ele

result = map(square, li)
print(result) #<map object at 0x1009d7130>

print(list(result)) #[1, 4, 9, 16]

li2 = ['10', '20', '30', '40']
print(li2) #['10', '20', '30', '40']
new_li = list(map(int,li2))
print(new_li) #[10, 20, 30, 40]

li3 = [1,2,3,0]
print(list(map(float,li3))) #[1.0, 2.0, 3.0, 0.0]

print(list(map(bool,li3))) #[True, True, True, False]
