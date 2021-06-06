import math

def volume(option):
    if option == 1:
        radio = float(input('Cual es el radio del cilindro? '))
        h = float(input('Cual es la altura del cilindro? '))
        V = math.pi * radio**2 * h
        print(f'El volumen del cilindro es {V} U^3\n')
    elif option == 2:
        radio = float(input('Cual es el radio de la esfera? '))
        V = 3/4 * math.pi * radio**3
        print(f'El volumen de la esfera es {V} U^3\n')
    elif option == 3:
        lado = float(input('Cual es la longitud de lado del cubo? '))
        V = lado**3
        print(f'El volumen del cubo es {V} U^3\n')
    elif option == 4:
        base = float(input('Cual es la longitud de la base de la piramide? '))
        h = float(input('Cual es la altura de la piramide? '))
        V = 1/3 * base**2 * h
        print(f'El volumen de la piramide es {V} U^3\n')
    elif option == 5:
        Radio = float(input('Cual es el radio MAYOR del toroide? '))
        radio = float(input('Cual es el radio MENOR del toroide? '))
        if Radio > radio:
            V = 2*(math.pi)**2 * radio**2 * Radio
            print(f'El volumen del Toroide es {V} U^3\n')
        else:
            print('El radio Menor es mas grande que el radio Mayor, prueba de nuevo')
        

if __name__ == '__main__':
    option = int(input(''' 
                          Escoge el Volumen de la figura deseada

                        [1] Cilindro
                        [2] Esfera
                        [3] Cubo
                        [4] Piramide
                        [5] Toroide
                                                                    '''))
    if (option==1 or option==2 or option==3 or option==4 or option==5):
        volume(option)
    else:
        print('Elige una opcion valida')
