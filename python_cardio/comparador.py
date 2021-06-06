def comparador():
    n1 = float(input('Ingresa el limite SUPERIOR '))
    n2 = float(input('Ingresa el limite INFERIOR '))
    n3 = float(input('Ingresa el numero a comparar '))

    while True:
        if n3 > n1 :
            print(f'\nEl numero ingresado {n3} supero el limite superior')
            n3 = float(input('Ingresa el numero a comparar'))
        elif n3 < n2:
            print(f'\nEl numero ingresado {n3} es menor al limite inferior')
            n3 = float(input('Ingresa el numero a comparar'))
        else:
            print(f'\nEl numero {n3} esta en el rango')
            break


if __name__ == '__main__':
    print('''
                Este programa es un comparador de numeros

            Deberas ingresar 3 numeros, uno sera el limite mayor
            otro sera el limite menor, y el tercero debe ser un 
            numero dentro del rango para terminar el programa.

    ''')

    comparador()