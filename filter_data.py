DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():

    # Obtener programadores de Python
    # Con list comprehension
    all_python_devs = [i["name"] for i in DATA if i["language"] == 'python']

    for worker in all_python_devs:
        print(f'LC {worker}')

    # Con funcion orden superior
    all_python_devs_os = list(filter(lambda x: x['language'] == 'python', DATA))
    all_python_devs_os = list(map(lambda x: x['name'], all_python_devs_os))

    for worker in all_python_devs_os:
        print(f'FOS {worker}')

    print('\n')

    # Obtener trabajadores de Platzi
    # Con list comprehension
    all_platzi_workers = [i["name"] for i in DATA if i["organization"] == 'Platzi']

    for worker in all_platzi_workers:
        print(f'LC {worker}')

    # Con funcion orden superior
    all_platzi_workers_os = list(filter(lambda x: x['organization'] == 'Platzi', DATA))
    all_platzi_workers_os = list(map(lambda x: x['name'], all_platzi_workers_os))

    for worker in all_platzi_workers_os:
        print(f'FOS {worker}')
    
    print('\n')

    # Obtener a todas aquellas personas mayores de 18 años
    # Con list comprehension
    adults = [i['name'] for i in DATA if i['age'] > 18]

    for worker in adults:
        print(f'LC {worker}')

    # Con funcion orden superior
    adults_os = list(filter(lambda x: x["age"] > 18, DATA))
    adults_os = list(map(lambda x: x['name'], adults_os))

    for worker in adults_os:
        print(f'FOS {worker}')

    # Agregar al diccionario nuevo valor "Old" cuyo valor sera True o False dependiendo si es mayor o no de 18 años
    # El valor | en Python funciona como un + en listas
    old_people = list(map(lambda x: x | {'old': x['age'] > 18}, DATA))

if __name__ == '__main__':
    run()