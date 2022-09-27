
def main():
    vehiculo = Vehiculo('KDR-888',4, 'sentra', 'nissan', 2010)
    archivo = open('vehiculo.txt', 'w')
    archivo.write(vehiculo.jsonStr())
    archivo.close()
    archivo = open('vehiculo.txt', 'r')
    print(archivo.read())
    archivo.close()

class Vehiculo:
    def __init__(self, placa, pasajeros, modelo, marca, año) -> None:
        self.placa = placa
        self.pasajeros = pasajeros
        self.modelo = modelo
        self.marca = marca
        self.año = año

    def jsonStr(self) -> str:
        return f'placa: {self.placa},\npasajeros: {self.pasajeros},\nmodelo: {self.modelo},\nmarca: {self.marca},\naño: {self.año}'

if __name__ == '__main__':
    main()