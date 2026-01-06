# Soma de A e B
def funcaoret(a, b):
    return a + b
print("A soma de A e B:",funcaoret(20,30))

# Filtrando listas para uma soma total
def somarlista(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total
lista = [10, 20, 30, 40]
print("A soma total:",somarlista(lista))

# Filtrando números em pares
def funcaopar(lista):
    pares = []            # Nova lista vazia
    for numero in lista:    # Percorre a lista original
        if numero % 2== 0:  # Verifica se é par
            pares.append(numero)    # Adiciona na nova lista
    return pares    # Retorna no final
listapares = [10, 20, 30, 40]
print("Os pares são:",funcaopar(listapares))



