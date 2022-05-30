from functools import reduce

# Multiplicar cada elemento de la lista por el siguiente

# Con ciclo for

def multip_elements(lista):
    aux = 1

    for i in lista:
        aux = aux * i

    print(aux)

# Con reduce

def multip_elements_reduce(lista):
    """
    Funcionamiento del reduce: (Ejemplo lista [2, 2, 2, 2, 2])
        1. Primera iteracion: Primer valor por segundo valor (2 * 2)
        2. Segunda iteracion: Resultado de la operacion anterior por tercer valor (4 * 2)
        3. Tercera iteracion: Resultado de la operacion anterior por cuarto valor (8 * 2)
        4. Asi sucesivamente
    
    """
    aux = reduce(lambda a, b: a * b, lista)
    
    print(aux)

if __name__ == '__main__':
    list_size = int(input("Ingrese el tamaño de la lista: "))
    list_value = []

    for i in range(list_size):
        list_value.append(int(input("Ingrese el valor: ")))

    multip_elements(list_value)
    multip_elements_reduce(list_value)
