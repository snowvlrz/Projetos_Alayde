print('\n Folha de Pagamento \n')
# o usuário tem que digitar:
nomefunc = str(input('Digite o nome do funcionário: '))
salario = int(input('Digite o salário desse funcionário: '))
filhos = int(input('Digite o número de filhos que o funcionário possui: '))
atraso = int(input('Digite quantas horas esse funcionário atrasou: '))
extra = int(input('Digite a quantidade de horas extra esse funcionário fez: '))
print('\n Relatório de Entrada: \n INSS = 8% \n V.T (Vale Transporte) = 6% \n V.R (Vale Refeição) = 5% \n P.S (Plano de Saúde) = 12% \n')
valor_hora = salario / 160
horaextra = ( (valor_hora + (valor_hora * 0.5)) * extra )
atrasodesc = valor_hora * atraso
quantfilhos = salario + 65
# descontos fixos
INSS = (salario*0.08)
VT = (salario*0.06)
VR = (salario*0.05)
PS = (salario*0.12)

print('Valor hora extra = 50%')
print('Bonus de quem não tem atraso: 5%')

salariobase = salario - INSS - VT - VR - PS - atrasodesc + horaextra

if atraso == 0:
    bonus = salario * 0.05
else:
    bonus = 0
if filhos == 0:
 quantfilhos = salario + 65.00
else:
   quantfilhos = 0 

salarioliquido = salariobase + bonus

# saída de dados
print('\n Relatório de Saída \n ')
print('Desconto INSS: R$ ', INSS)
print('Desconto VT: R$', VT)
print('Desconto VR: R$', VR)
print('Desconto PS: R$', PS)
print('Desconto por atraso: R$', atrasodesc)
print('Valor das horas extras: R$', horaextra)
print('Bônus de sem atraso: R$', bonus)
print('Adicional por filho: R$', quantfilhos)
print('Salário líquido do funcionário', nomefunc, 'é: R$', salarioliquido)