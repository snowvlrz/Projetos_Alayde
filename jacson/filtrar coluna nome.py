import pandas as pd

# Lê o arquivo CSV com os dados dos alunos
df_alunos = pd.read_csv("alunos.csv", encoding="utf-8")

# Exibe apenas a coluna 'nome'
print("Coluna 'nome' do arquivo alunos.csv:")
print(df_alunos['nome'])
