class Dog:
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
        print(f'{raca} criado.')

    def envelhecer(self):
        self.idade += 1
        return print(self.idade)
dog = Dog('Lab')
dog.idade = 11
print(dog.idade)
print(dog.raca)
print('')

dog2 = Dog('Huskie')
print(dog2.idade)
print(dog2.raca)
print('')

dog.envelhecer()

