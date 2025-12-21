numeros = [10, 20, 30, 40, 50]

# Mostrar número especifíco
print(numeros[2])

#For de 1 a 10
for numeros in range(1,11):
    print(numeros)

#while de 1 a 20
while numeros >=30:
    print(numeros)

#For com um if embutido ao meio em pares
for pares in numeros:
    if numeros % 2==0:
        print(pares)

# Mostrar todos
for numero in numeros:
    print(numero)

# Maiores que 25
for numero in numeros:
    if numero > 25:
        print("Maior que 25:", numero)

# Soma
total = 0
for numero in numeros:
    total += numero

print("Soma total:", total)

