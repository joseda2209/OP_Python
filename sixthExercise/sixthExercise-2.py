class Alumno: 
    def __init__(self, nombre, nota) -> None:
        self.nombre = nombre
        self.nota = nota
    def is_aproved(self) -> str:
        return f'el alumno {self.nombre} {"NO" if self.nota < 3.0 else "SI"} aprobo'

nombreInput = input('Ingrese el nombre del alumno: ')
notaInput = float(input('Ingrese la nota del alumno: '))
alumno = Alumno(nombreInput, notaInput)
print(alumno.is_aproved())
