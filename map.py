# Elevar al cuadrado cada elemento de la lista

# Con comprehension

def squares_comprehension(lista):
    square = [i**2 for i in lista]
    print(square)

# Con map

def squares_map(lista):
    square = list(map(lambda x: x**2, lista))
    print(square)

if __name__ == '__main__':
    list_size = int(input("Ingrese el tamaño de la lista: "))
    list_value = []

    for i in range(list_size):
        list_value.append(int(input("Ingrese el valor: ")))

    squares_comprehension(list_value)
    squares_map(list_value)
