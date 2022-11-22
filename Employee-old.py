# create a class
class Employee:

    # class attributes
    os = 'Windows 2010'
    work_style = 'remote'
    hourly_salary = 15

    # constructor method / initializer
    # build the objects
    def __init__(self, name, role, is_manager, location = 'New York'):
        self.name = name
        self.role = role
        self.is_manager = is_manager
        self.location = location
    
    def bio(self):
        print(f'Hello! My name is {self.name} I am a {self.role} and I am located in work in {self.location} branch. I use {self.os}.')

# create object/instance
Marian = Employee('Marian', 'Developer', False, 'Singapore')
Bob = Employee('Bob', 'QA', True)
Bob.bio()

