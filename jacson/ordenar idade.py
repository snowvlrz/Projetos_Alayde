import pandas as pd

# Lê o arquivo CSV
df_alunos = pd.read_csv("alunos.csv", encoding="utf-8")

# Ordena pela coluna idade em ordem decrescente
df_ordenado = df_alunos.sort_values(by='idade', ascending=False)

# Exibe o resultado
print("DataFrame ordenado por idade (decrescente):")
print(df_ordenado)
