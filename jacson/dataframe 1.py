import pandas as pd

# Dados dos 5 alunos
dados = {
    'nome': ['Ana', 'Bruno', 'Carla', 'Diego', 'Eduarda'],
    'idade': [17, 18, 16, 19, 17]
}

# Cria DataFrame
df = pd.DataFrame(dados)

# Exibe DataFrame
print("DataFrame criado (5 alunos):")
print(df)

