
def conversor(cantidad, operacion):
    if (operacion == 1):
        millas = cantidad / 1.609344
        print(f'\nLa cantidad {cantidad} kilometros equivale a {millas} millas\n')
    elif(operacion ==2):
        km = cantidad * 1.609344
        print(f'\nLa cantidad {cantidad} millas equivale a {km} kilometros\n')
    



if __name__ == '__main__':
    cantidad = float(input('''
                        *****   C O N V E R S O R  D E  D I S T A N C I A S ****
                               

                                Ingresa la magnitud de la distancia a convertir             
                        '''))

    operacion = int(input('''
                                Ingresa la conversion a realizar:

                                [1] Kilometros a Millas
                                [2] Millas a Kilometros
                        '''))
    if (operacion == 1 or operacion == 2):
        conversor(cantidad, operacion)
    else:
        print('\nEscoge una opcion valida')