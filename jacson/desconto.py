produtos = []
total = 0

while True:
    preco = input("Digite o preço do produto (ou 'fim' para encerrar): ")
    if preco.lower() == 'fim':
        break
    total += float(preco)

if total <= 100:
    desconto = 0.10
elif total <= 500:
    desconto = 0.20
else:
    desconto = 0.30

valor_final = total * (1 - desconto)
print(f"Total da compra: R${total:.2f}")
print(f"Desconto aplicado: {desconto*100:.0f}%")
print(f"Valor final a pagar: R${valor_final:.2f}")
