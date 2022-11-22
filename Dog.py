from Mammal import Mammal

class Dog(Mammal):
    
    legs = 4

    # class attributes
    def __init__(self, name, age, breed):
        self.name = name
        self.breed = breed
        self.age = age
    
    def bark(self):
        if self.age < 1:
            print('Cheey, Cheey!!!')
        else:
            print('Whoof, Whoof!!!')


Rocky = Dog('Rocky', 0.5, 'Huskie')
Cooper = Dog('Cooper', 4, 'Bulldog')

print(Rocky.feeds_milk)
Rocky.bio()