# Criando dados e fazendo chamadas
aluno = {
    "nome": "Samuel",
    "idade": 22,
    "curso": "ADS"
}
print(aluno["nome"])
print(aluno["idade"])
print(aluno["curso"])

# Usando o for para filrar dados em colchete(chave-valor)
for chave, valor in aluno.items():
    print(chave, ":", valor)
