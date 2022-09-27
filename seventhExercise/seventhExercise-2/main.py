import time

def main():
    hourInput=input('ingrese la hora a validar o -1 para usar la hora del sistema (24H): ')
    if hourInput == '-1':
        now = time.localtime()
    else:
        now = time.strptime(hourInput, '%H')
    if now.tm_hour > 19:
        print('Es momento de ir a casa')
    else:
        leftTime = 19 - now.tm_hour
        print(f'Faltan {leftTime} para salir del trabajo')


if __name__ == '__main__':
    main()