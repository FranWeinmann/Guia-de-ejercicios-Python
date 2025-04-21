def obtener_numeros_pares(lista):
    pares = []
    for number in lista:
        if number % 2 == 0:
            pares.append(number)
    return pares

userNumbers = input('Ingrese una lista de números: ')

numbers = [int(num.strip()) for num in userNumbers.split(",")]

numeros_pares = obtener_numeros_pares(numbers)
print('Los nummeros pares de tu lista, son: ', numeros_pares)