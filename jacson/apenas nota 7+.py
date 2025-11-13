import pandas as pd

# Lê o arquivo CSV
df_alunos = pd.read_csv("alunos.csv", encoding="utf-8")

# Filtra alunos com nota > 7
alunos_aprovados = df_alunos[df_alunos['notas'] > 7]

# Exibe o resultado
print("Alunos com nota maior que 7:")
print(alunos_aprovados)
