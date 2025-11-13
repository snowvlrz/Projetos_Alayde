import pandas as pd

# Lê o arquivo alunos.csv
df_alunos = pd.read_csv("alunos.csv", encoding="utf-8")

# Exibe apenas os 5 primeiros registros
print("Primeiros 5 registros do arquivo alunos.csv:")
print(df_alunos.head())
