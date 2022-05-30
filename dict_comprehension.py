# Dictionary comprehension: Crear un diccionario cuyas llaves sean los 1000 primeros numeros naturales con sus raices cuadradas como valores.

import math

def run():
    natural_numbers = {i: math.sqrt(i) for i in range(1, 1001)}

    print(natural_numbers)

if __name__ == '__main__':
    run()