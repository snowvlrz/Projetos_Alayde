print("Olá usuário!")  # Imprime a mensagem inicial
num1 = int(input("Digite o primeiro número: "))  # Lê o primeiro número
num2 = int(input("Digite o segundo número: "))  # Lê o segundo número

resultado = 0  # Inicializa o resultado da multiplicação
for i in range(num2):  # Repete num2 vezes
    resultado += num1  # Soma num1 ao resultado (simula multiplicação)

print(f"{num1} x {num2} = {resultado}")  # Exibe o resultado da multiplicação