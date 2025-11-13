import random # importa a biblioteca "Aleatório"

numeropc = random.randint(1, 20) # Faz com que o computador escolha um número aleatório entre 1 e 20
print("Olá usuário!") # Imprime no terminal o texto digitado
print("Tente adivinhar o número que o programa escolheu.") # Imprime no terminal o texto digitado

while True: # "Enquanto for verdadeiro, ou seja, enquanto o usuário não acertar..."
    tentativa = int(input("Digite seu palpite: ")) # Cria uma variável para o usuário dar o palpite

    if tentativa == numeropc: # Se o palpite for igual o número escolhido pelo computador...
        print("Parabéns, você acertou!") # O usuário acertou
        break # Finaliza o programa
    elif tentativa > numeropc: # Se o palpite for maior que o número escolhido pelo computador...
        print("Você errou. O número é menor.") # Imprime esse texto e continua o jogo
    elif tentativa < numeropc: # Se o palpite for menor...
        print("Você errou. O número é maior.") # Imprime esse texto e continua o jogo
