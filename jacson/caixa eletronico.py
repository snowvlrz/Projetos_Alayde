print("Olá usuário!")
valor = int(input("Digite o valor: "))  # Pede o valor em número inteiro pro usuário

notas = [100, 50, 20, 10, 5]  # Lista com os valores das notas disponíveis

for nota in notas:  # Para cada tipo de nota na lista
    quantidade = valor // nota  # Calcula quantas notas desse valor cabem no valor restante
    if quantidade > 0:  # Se precisa de pelo menos uma nota desse valor
        print(f"Notas de {nota}: {quantidade}")  # Mostra quantas notas são necessárias
    valor = valor % nota  # Atualiza o valor restante (resto da divisão)