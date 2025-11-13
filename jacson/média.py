print("Olá usuário!") # Imprime no terminal o texto digitado
n1 = float(input("Digite a primeira nota em decimal. (Ex: 0.0): ")) # cria uma variável para o usuário digitar a primeira nota
n2 = float(input("Digite a segunda nota em decimal. (Ex: 0.0): ")) # cria uma variável para o usuário digitar a segunda nota
n3 = float(input("Digite a segunda nota em decimal. (Ex: 0.0): ")) # cria uma variável para o usuário digitar a terceira nota
média = (n1+n2+n3)/3 # faz o cálculo

if média >=6: # se a média for maior ou igual a 6...
 print("A média é: ", média, "e o aluno está aprovado.") # Imprime no terminal o texto digitado com o resultado

else: # senão...
 print("A média é: ", média, "e o aluno está reprovado.") # Imprime no terminal o texto digitado com o resultado