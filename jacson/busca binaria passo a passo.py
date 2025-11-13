numeros = [3, 7, 12, 19, 23, 28, 33, 36, 40, 45, 49, 52, 60, 65, 72, 78, 81, 87, 93, 99]
num = int(input("Digite o número que deseja buscar: "))

inicio = 0
fim = len(numeros) - 1
passo = 1
encontrado = -1

while inicio <= fim:
    meio = (inicio + fim) // 2
    print(f"Passo {passo}: Lista atual = {numeros[inicio:fim+1]}, meio = {numeros[meio]}")
    passo += 1

    if numeros[meio] == num:
        encontrado = meio
        break
    elif numeros[meio] < num:
        inicio = meio + 1
    else:
        fim = meio - 1

if encontrado != -1:
    print(f"\nNúmero {num} encontrado na posição {encontrado}.")
else:
    print(f"\nNúmero {num} não encontrado na lista.")
