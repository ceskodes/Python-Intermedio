# List comprehension: Crear una lista de todos los multiplos de 4, 6 y 9 hasta 4 digitos.

def run():
    number = [i for i in range(1, 10000) if i % 36 == 0]

    print(number)

if __name__ == '__main__':
    run()