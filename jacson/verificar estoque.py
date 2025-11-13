produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i+1}: ")
    quantidade = int(input(f"Digite a quantidade de {nome}: "))
    produtos[nome] = quantidade

print("\nProdutos com quantidade inferior a 10:")
for nome, quantidade in produtos.items():
    if quantidade < 10:
        print(f"{nome}: {quantidade} unidades")
