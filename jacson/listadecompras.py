lista = []
print("Olá usuário") # Imprime no terminal o texto digitado
print("Digite 5 itens para a lista: ") # Imprime no terminal o texto digitado

for i in range(5): # continua pedindo itens até que haja 5 na lista
    item = input(f"Digite o item {i+1}: ") # Campo para que o usuário digite o item, enquanto o {i+1} vai dizendo qual o item que está sendo digitado, ou seja: item 1, item 2...
    lista.append(item) # adiciona o item na lista salva

print("\n A lista final é: ") # Imprime no terminal o texto digitado
for produto in lista: # pega os produtos que estão na lista
    print(f" - {produto}") # Imprime no terminal o texto digitado com o resultado