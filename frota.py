veiculo = str()
kmsaida = int()
kmchegada = int()

veiculo=str(input("Digite o veículo:"))
kmsaida=int(input("Digite a Quilometragem de Saída:"))
kmchegada=int(input("Digite a Quilometragem de Chegada:"))

quilometragem = (kmchegada - kmsaida)
print("A quilometragem rodada é:", quilometragem)
print("\n")

consumo = (quilometragem/16)
print("A quantidade de Litros consumidos é:", consumo)
print("\n")

valorpago = (consumo*5.99)
print("O valor de combustível pago é:R$", valorpago)
print("\n")
print("OBS: Valor do combustível = R$5,99", "\n", "Km p/ Litro = 16km")