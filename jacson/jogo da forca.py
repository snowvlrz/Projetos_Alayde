import random

print("Olá usuário!")
palavras = ['python', 'programacao', 'computador', 'jogo', 'forca', 'amigo', 'exilio', 'psicologia', 'filosofia']
palavra = random.choice(palavras).upper()
letras_certas = []
letras_erradas = []
tentativas = 6

while tentativas > 0:
    palavra_oculta = ''.join([letra if letra in letras_certas else '_' for letra in palavra])
    
    print(f'\nPalavra: {palavra_oculta}')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    print(f'Tentativas restantes: {tentativas}')
    
    if '_' not in palavra_oculta:
        print('\nParabéns! Você ganhou!')
        break
    
    entrada = input('Digite uma letra ou a palavra completa: ').upper()
    
    if entrada == palavra:
        print('\nParabéns! Você acertou a palavra completa!')
        break
    
    if len(entrada) > 1:
        print('Palavra incorreta!')
        tentativas -= 1
        continue
    
    letra = entrada
    
    if letra in letras_certas or letra in letras_erradas:
        print('Você já tentou essa letra!')
        continue
    
    if letra in palavra:
        letras_certas.append(letra)
        print('Acertou!')
    else:
        letras_erradas.append(letra)
        tentativas -= 1
        print('Errou!')
        

if tentativas == 0:
    print(f'\nVocê perdeu! A palavra era: {palavra}')