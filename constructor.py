class Employee:
    def __init__(self):      #Constructor of class Employee
        self.emp_name = 'AK' #Instance Variables
        self.emp_id = 101    #Instance Variables

#Creating Objects:
e1 = Employee()

#Accessing Properties of e1 Object:
print('Employee name for e1 is:',e1.emp_name)
print('Employee ID for e1 is:',e1.emp_id)

e2 = Employee()
print('Employee name for e2 is:',e2.emp_name)
print('Employee ID for e2 is:',e2.emp_id)