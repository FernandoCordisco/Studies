class Animal:
    def __init__(self):
        print('Animal criado.')

    def quem_sou_eu(self):
        print('Eu sou um animal.')

    def comer(self):
        print('Comendo.')

animal1 = Animal()
animal1.quem_sou_eu()
print('')


class Dog(Animal):
    def quem_sou_eu(self):
        print('Eu sou um cachorro.')

dog1 = Dog() 
dog1.quem_sou_eu()
print('')