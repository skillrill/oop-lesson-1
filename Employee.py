from Human import Human

# create a class
class Employee(Human):

    # class attributes
    _os = 'Windows 2010'
    work_style = 'remote'
    hourly_salary = 15

    # constructor method / initializer
    # build the objects
    def __init__(self, role, is_manager, location = 'New York'):
        self.role = role
        self.is_manager = is_manager
        self.location = location
    
    def bio(self, name):
        print(f'Hello! My name is {name} I am a {self.role} and I am located in work in {self.location} branch. I use {self.os}.')

# create object/instance
Marian = Employee('Developer', False, 'Singapore')
Bob = Employee('QA', True)

Bob._os

class Other:
    os = Bob._os
    
# Human.evolution_length()
# Employee.evolution_length()
# Bob.evolution_length()

# Human.is_adult(4)
# Employee.is_adult(20)
# Bob.is_adult(19)

# Marian.legs
# Bob.speak()
# Marian.walk(4)

# Marian.bio('Marian')
# Bob.bio('Bob')

# print(Marian.location)
# print(Bob.location)


# print(Marian.role)
# print(Bob.is_manager)
# print(Bob.role)
















# Employee.hourly_salary = 16.75
# Marian.hourly_salary = 30
# Employee.hourly_salary = 18

# print(Marian.hourly_salary)
# print(Bob.hourly_salary)


# print(id(Employee.hourly_salary))
# print(id(Bob.hourly_salary))
# print(id(Marian.hourly_salary))













# print(Marian)
# print(Bob)
# print(type(Marian))
# print(type(Bob))
# print(type('ABC'))
# print(isinstance(Marian, Employee))
# print(isinstance('abc', str))
# print(isinstance(1000, int))
