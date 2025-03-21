d1 = {
    'name':'Priya', 
    'age':33,
    'phone': 34568,
    'Maths':90,
    'Science':90,
    'name': 'Ankit',
    'ID':101
    }

print(d1, type(d1))

#Accessing dict values:
print(d1['name']) #Ankit
print(d1['Maths']) #90

for i in d1.keys():
    print(i, end = "-")

'''name-age-phone-Maths-Science-ID-'''
print()

for i in d1.values():
    print(i, end = "-")
    
'''Ankit-33-34568-90-90-101-'''
print()

for i in d1.items():
    print(i)
'''
('name', 'Ankit')
('age', 33)
('phone', 34568)
('Maths', 90)
('Science', 90)
('ID', 101)
'''