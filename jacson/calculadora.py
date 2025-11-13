print("Olá usuário!") # Imprime no terminal o texto digitado
num1 = float(input("Digite o primeiro número: ")) # cria uma variável para o usuário digitar o primeiro número
op = input("Digite a operação: ") # cria uma variável para o usuário escolher a operaçao
num2 = float(input("Digite o segundo número: ")) # cria uma variável para o usuário digitar o segundo número
if op == "+": # define uma condição "se", onde se a operação for +...
    resultado = num1+num2 # soma os números
elif op == "-": # define uma condição "se", onde se a operação for -...
    resultado = num1-num2 # subtrai os números
elif op == "*": # define uma condição "se", onde se a operação for *...
    resultado = num1*num2 # multipkica os números
elif op == "/": # define uma condição "se", onde se a operação for /...
    if num2 != 0: # se o número 2 for diferente de 0, mostra o resultado
     resultado = num1/num2 # divide os números
    else: # senão...
       print("Impossível dividir por 0!") # mostra este texto
else:
   print("Operação inválida!") # se a operação escolhida não for as definidas ou estiverem erradas, mostra este texto.

print(f"Resultado: {resultado}") # mostra o resultado
