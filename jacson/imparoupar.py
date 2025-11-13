print('Boas vindas, usuário!') # Imprime no terminal o texto digitado
n = int(input('Digite um número: ')) # Cria uma variável para o usuário digitar o número
resto = n % 2 # divide o número por 2 e utiliza o resto

if resto == 1: # se o resto da divisão for 1....
    print('O número', n, 'é ímpar.') # Imprime no terminal o texto digitado com o resultado


elif resto == 0: # se o resto da divisão for 0...
    print('O número', n, 'é par.') # Imprime no terminal o texto digitado com o resultado