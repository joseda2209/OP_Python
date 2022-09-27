from calculator import calculator

def main():
    num1 = float(input('ingrese un numero: '))
    num2 = float(input('ingrese otro numero: '))
    print(f'los numeros ingresados son: {num1} y {num2}')
    print(f'la suma entre los dos numeros es: {calculator.suma(num1, num2)}')
    print(f'la resta entre los dos numeros es: {calculator.resta(num1, num2)}')
    print(f'la multiplicación entre los dos numeros es: {calculator.multiplicacion(num1, num2)}')
    print(f'la division entre los dos numeros es: {calculator.division(num1, num2)}')


if __name__ == '__main__':
    main()