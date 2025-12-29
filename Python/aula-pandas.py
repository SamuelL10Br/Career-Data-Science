#Primeiro contato (DataFrame)
import pandas as pd

dados = {
    "nome": ["Samuel", "Ana", "José"],
    "idade": [22, 39, 24],
    "profissão": ["Cientista de Dados", "Analista de Dados", "Desenvolvedor Mobile"]
}

df = pd.DataFrame(dados)
print(df)

#Acessando colunas
print(df["nome"])

#Ou
print(df["idade"])

#Filtrando dados (O poder do pandas)
#Pessoas maiores de idade:
maiores = df[df["idade"] >= 18]
print(maiores)

#Pessoas com idade >= 30:
print(df[df["idade"] >= 30])

#Selecionando colunas + filtro
print(df[df["idade"] >= 30][["nome", "profissao"]])

#Lendo CSV com pandas
df = pd.read_csv("dados.csv")
print(df)

#Exemplo completo
import pandas as pd

# Lendo CSV
df = pd.read_csv("dados.csv")

print("Dados completos:")
print(df)

print("\nPessoas com idade >= 30:")
print(df[df["idade"] >= 30])

print("\nApenas nome e profissão:")
print(df[["nome", "profissao"]])


