# Filtrar numeros impares con list comprehension

def odd_comprehension(lista):
    odd = [i for i in lista if i % 2 != 0]

    print(odd)

# Filtrar numeros impares con filter y lambda function

def odd_lambda(lista):
    odd = list(filter(lambda x: x%2 != 0, lista))

    print(odd)

if __name__ == '__main__':

    list_size = int(input("Ingrese el tamaño de la lista: "))
    list_value = []

    for i in range(list_size):
        list_value.append(int(input("Ingrese el valor: ")))

    odd_comprehension(list_value)
    odd_lambda(list_value)
