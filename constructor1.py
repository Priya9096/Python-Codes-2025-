class Employee:
    def __init__(self,name, id):
        self.emp_name = name
        self.emp_id = id

#Creating Object:
e1 = Employee('AK',101)
e2 = Employee('PK',102)

#Accessing Properties of e1 Object:
print('Employee name of e1 is: ',e1.emp_name)
print('Employee ID of e1 is: ',e1.emp_id)


#Accessing Properties of e2 Object:
print('Employee name of e2 is: ',e2.emp_name)
print('Employee ID of e2 is: ',e2.emp_id)

