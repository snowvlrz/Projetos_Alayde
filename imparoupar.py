print('Boas vindas, usuário!')
n = int(input('Digite um número: '))
resto = n % 2

if resto == 1:
    print('O número', n, 'é ímpar.')


elif resto == 0:
    print('O número', n, 'é par.')
