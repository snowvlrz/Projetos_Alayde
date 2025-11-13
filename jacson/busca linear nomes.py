nomes = [
    "Ana", "Bruno", "Carlos", "Daniela", "Eduardo", "Fernanda", "Gabriel",
    "Helena", "Isabela", "João", "Karen", "Lucas", "Mariana", "Nathalia", "Otávio"
]
busca = input("Digite o nome que deseja procurar: ")
encontrado = -1
for i in range(len(nomes)):
    if nomes[i].lower() == busca.lower():
        encontrado = i
        break

if encontrado != -1:
    print(f"O nome '{busca}' foi encontrado na posição {encontrado}.")
else:
    print(f"O nome '{busca}' não foi encontrado na lista.")
