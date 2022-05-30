# Funcion palindromo en codigo normal
def palindrome(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    
# Funcion palindromo en lambda function

def run():
    palindrome = lambda string: string == string[::-1]
    print(palindrome('ana'))

if __name__ == '__main__':
    run()
    print(palindrome('Ana'))