def divisors(num):
    try:
        if num < 0 or num == 0:
            # Arrojara un error si el numero es negativo o 0
            raise ValueError("Debes ingresar un numero entero mayor o igual que 1.")
        divisors = []

        # Verificara si en la lista existe multiplos de num
        for i in range(1, num + 1):
            if num % i == 0:
                divisors.append(i)
        return divisors
    except ValueError as ve:
        print(ve)


def run():
    # El Try Except verificara que se ingrese unicamente numeros
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un numero entero mayor o igual que 1.")


if __name__ == '__main__':
    run()