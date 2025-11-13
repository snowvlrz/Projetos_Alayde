print("Olá usuário!")
horas = int(input("Digite quantas horas você trabalhou: "))
valorhora = float(input("Digite quanto ganha por hora em reais (R$): "))
salário = horas*valorhora
bonus = salário+(salário*0.15)
print("Você receberá", salário, "reais de salário e", bonus, "reais de bônus.")
