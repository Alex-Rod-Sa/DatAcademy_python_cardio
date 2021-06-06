import math

def run():
    b = float(input('Escribe la Base del triangulo: '))
    h = float(input('Escribe la Altura del triangulo: '))
    x = float(input('En que punto fue tomada la altura?: '))
    if(x < 0):
        print('Ingresa un numero positivo ')
    else:
        A = (b * h) / 2.0
        print(f'\nEl area del triangulo es {A}')
        

        if (x == 0 or x == b):
            c = round(math.sqrt(b**2 + h**2), 1)
            if (b == c or b == h or h == c):
                print('Es un triangulo Isoseles, ya que dos de sus lados son iguales')
            else:
                print('Es un triangulo Escaleno, ya que ninguno de los lados es igual')

        if (x == b/2):
            c = round(math.sqrt((b/2)**2 + h**2), 1)
            if (b == c):
                print('Es un triangulo Equilatero, ya que todos sus lados son iguales')
            else:
                print('Es un triangulo Isoseles, ya que dos de sus lados son iguales')

        else:
            if (x < b):
                b1 = x
                b2 = x - b 
                print(b2)
                c1 = round(math.sqrt((b1)**2 + h**2), 1)
                c2 = round(math.sqrt((b2)**2 + h**2), 1)
                if(b == c1 or b == c2):
                    print('Es un triangulo Isoseles, ya que dos de sus lados son iguales')
                else:
                    print('Es un triangulo Escaleno, ya que ninguno de los lados es igual')
            else:
                b1 = x
                b2 = b - x
                c1 = round(math.sqrt((b1)**2 + h**2), 1)
                c2 = round(math.sqrt((b2)**2 + h**2), 1)
                if(b == c1 or b == c2):
                    print('Es un triangulo Isoseles, ya que dos de sus lados son iguales')
                else:
                    print('Es un triangulo Escaleno, ya que ninguno de los lados es igual')


if __name__ == '__main__':
    print(''' 
                   Este programa calcula el area de un triangulo
    
                                                                ''')
    run()
