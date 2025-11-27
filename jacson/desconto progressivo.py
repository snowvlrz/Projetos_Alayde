def calcular_desconto(total):
    if total <= 100:
        perc = 5
    elif total <= 300:
        perc = 10
    else:
        perc = 15
    desconto = total * perc / 100
    final = total - desconto
    return perc, desconto, final

def main():
    try:
        total = float(input("Valor total da compra (R$): ").replace(",","."))
    except ValueError:
        print("Entrada inválida. Use um número (ex: 250.50).")
        return

    perc, desconto, final = calcular_desconto(total)
    print("\n--- Resumo da compra ---")
    print(f"Valor original: R$ {total:.2f}")
    print(f"Percentual de desconto aplicado: {perc}%")
    print(f"Valor do desconto: R$ {desconto:.2f}")
    print(f"Valor final a pagar: R$ {final:.2f}")

if __name__ == "__main__":
    main()
