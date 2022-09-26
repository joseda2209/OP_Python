class Vehiculo:
    def __init__(self, color, ruedas, puertas) :
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

    def __str__(self) -> str:
        print(f'color: {self.color}, ruedas: {self.ruedas}, puertas: {self.puertas}')

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self) -> str:
        super().__str__()
        print(f'velocidad: {self.velocidad}, cilindrada: {self.cilindrada}')

coche = Coche('rojo', 4, 4, 60, 1600)
coche.__str__()