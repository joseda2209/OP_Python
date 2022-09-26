#  un año es bisiesto si es divisible entre 400 o si es divisible por 4 y no por 100

def isLeapYear(year):
    if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0) ) :
        print(f'el año {year} es bisiesto')
    else: 
        print(f'el año {year} no es bisiesto')

yearInput = int(input('ingrese el año para conocer si es bisiesto: '))
isLeapYear(yearInput)