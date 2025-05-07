class Circle:
    def __init__(self, raio=1):
        self.raio = raio

    def calcula_area(self):
        return print(self.raio * self.raio * 3.14)
    
    def retorna_raio(self):
        return print(self.raio)
    
c1 = Circle()
c1.retorna_raio()
c1.calcula_area()


c2 = Circle(2)
c2.retorna_raio()
c2.calcula_area()        