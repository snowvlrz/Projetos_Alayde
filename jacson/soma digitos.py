print("Olá usuário!")  # Imprime a mensagem inicial
numero = input("Digite um número inteiro: ")  # Lê o número como string (texto)

soma = 0  # Inicializa a variável que vai armazenar a soma
for digito in numero:  # Para cada caractere (dígito) no número
    soma += int(digito)  # Converte o dígito para inteiro e soma

print(f"A soma dos dígitos é: {soma}")  # Exibe o resultado da soma