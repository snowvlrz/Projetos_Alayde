import pandas as pd

# Lê o arquivo CSV
df_alunos = pd.read_csv("alunos.csv", encoding="utf-8")

# Calcula média, mínimo e máximo da coluna notas
media = df_alunos['notas'].mean()
minimo = df_alunos['notas'].min()
maximo = df_alunos['notas'].max()

# Exibe os resultados
print("Estatísticas da coluna 'notas':")
print(f"Média: {media:.2f}")
print(f"Valor mínimo: {minimo}")
print(f"Valor máximo: {maximo}")
