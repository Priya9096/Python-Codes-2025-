class Student:
    college_name = "ABC University"
    
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    
    @classmethod
    def change_college_name(cls, new_name):
        cls.college_name = new_name  # Modifying class attribute using class method

    def attend_class(self):
        print(f"{self.name} from {Student.college_name} is attending the class.")

# Changing the class attribute using a class method
Student.change_college_name("XYZ University")

# Creating Student objects
student_1 = Student('Amit', 20, 'S123')
student_2 = Student('Priya', 19, 'S124')

student_1.attend_class()
student_2.attend_class()

# Accessing class method using an object reference
student_1.change_college_name("New University Name")

# Accessing class attribute directly through class name
print(Student.college_name)