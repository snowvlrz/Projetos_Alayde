def calcular_media(n1, n2, n3):
    peso_total = 2 + 3 + 5
    media = (n1*2 + n2*3 + n3*5) / peso_total
    return media

def situacao(media):
    if media >= 5.0:
        return "APROVADO"
    elif media >= 3.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"

def main():
    try:
        n1 = float(input("Nota 1 (N1) - peso 2: ").replace(",","."))
        n2 = float(input("Nota 2 (N2) - peso 3: ").replace(",","."))
        n3 = float(input("Nota 3 (N3) - peso 5: ").replace(",","."))
    except ValueError:
        print("Entrada inválida. Use números (ex: 7.5).")
        return

    media = calcular_media(n1, n2, n3)
    estado = situacao(media)

    print("\n--- Resultado ---")
    print(f"Média final (ponderada): {media:.2f}")
    print(f"Situação do aluno: {estado}")

if __name__ == "__main__":
    main()
