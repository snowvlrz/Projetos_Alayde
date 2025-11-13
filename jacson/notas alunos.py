import random
notas = [round(random.uniform(0, 10), 2) for _ in range(25)]
print("Notas originais:")
print(notas)
print("\nEscolha o método de ordenação:")
print("1 - Inserção (Insertion Sort)")
print("2 - Bolha (Bubble Sort)")
op = input("Opção: ")

if op == "1":
    # ordenação por inserção
    for i in range(1, len(notas)):
        chave = notas[i]
        j = i - 1
        while j >= 0 and notas[j] > chave:
            notas[j + 1] = notas[j]
            j -= 1
        notas[j + 1] = chave
elif op == "2":
    # ordenação bolha
    for i in range(len(notas) - 1):
        for j in range(len(notas) - 1 - i):
            if notas[j] > notas[j + 1]:
                notas[j], notas[j + 1] = notas[j + 1], notas[j]
else:
    print("Opção inválida.")
    exit()

print("\nNotas em ordem crescente:")
print(notas)

# exibir posição e status de aprovação
print("\nSituação dos alunos:")
for i, nota in enumerate(notas):
    status = "Acima da média" if nota >= 7 else "Abaixo da média"
    print(f"Posição {i}: Nota = {nota} -> {status}")
