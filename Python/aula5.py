# Função simples
def saudacao():
    print("Olá, bem-vindo!")
saudacao()

# Função com parâmetro
def mostrar_nome(nome):
    print("Seu nome é:", nome)
mostrar_nome("Samuel")

# Função que retorna valor
def somar(a, b):
    return a + b
resultado = somar(10, 20)
print("Resultado:", resultado)

# Um exemplo real de dados
def soma_lista(numeros):
    total = 0
    for numero in numeros:
        total += numero 
    return total
lista = [10, 20, 30, 40]
print("Soma:", soma_lista(lista))

# Exemplo completo + filtragem
def filtrar_maiores_que_25(numeros):
    for numero in numeros:
        if numero > 25:
            print(numero)
numeros = [10, 20, 30, 40, 50]
filtrar_maiores_que_25(numeros)