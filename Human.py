class Human:

    eyes = 2
    legs = 2
    
    @staticmethod
    def evolution_length():
        print('It took 55 million years')
    
    def is_adult(age):
        print(age > 18)

    def speak(self):
        print('I can speak')
    
    def walk(self, steps):
        print(f'Walked {steps} steps')