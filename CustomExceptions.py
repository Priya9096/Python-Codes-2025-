class InvalidAge(Exception):
    pass

def checkAge(age):
    if age<18:
        raise InvalidAge("Age must be greater than 18")
    
try:
    checkAge(12)
except InvalidAge as e:
    print("Exception Occurred details are: ",e)