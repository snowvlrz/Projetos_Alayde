print("Bom dia, usuário!")
print("Pegando a escova e a pasta de dente...")
tem_pasta = input("Há pasta no frasco? (s/n): ").lower()
if tem_pasta == 's':
    print("Escovando os dentes...")
    print("Dentes escovados com sucesso!")
else:
    print("Fim - Não é possível escovar sem pasta")