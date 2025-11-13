print("Olá usuário!")
valor = float(input("Digite o valor do produto em reais (R$): "))
vendas = int(input("Digite o total de vendas: "))
total = valor*vendas
desconto = total*0.05
print("Você tem ", desconto, "reais de desconto nessa venda.")