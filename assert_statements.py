def divisors(num):
    # El assert verifica que la variable num sea mayor que 0
    assert num > 0, "Debes ingresar un numero mayor que 0"
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    # El assert verificara que la entrada haya sido un numero.
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes colocar un numero."
    print(divisors(int(num)))
    print("Terminó mi programa")



if __name__ == '__main__':
    run()