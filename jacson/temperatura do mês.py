def ler_temperaturas(n_dias=30):
    temps = []
    print(f"Digite as temperaturas médias dos {n_dias} dias (use ponto ou vírgula):")
    for i in range(1, n_dias+1):
        while True:
            val = input(f"Dia {i}: ").strip()
            try:
                t = float(val.replace(",","."))
                temps.append(t)
                break
            except ValueError:
                print("Entrada inválida. Digite um número (ex: 27.3).")
    return temps

def resumo_temperaturas(temps, limite=27.3):
    media = sum(temps) / len(temps)
    maior = max(temps)
    menor = min(temps)
    acima = sum(1 for t in temps if t > limite)
    return media, maior, menor, acima

def main():
    temps = ler_temperaturas(30)
    media, maior, menor, acima = resumo_temperaturas(temps, limite=27.3)
    print("\n--- Resumo mensal ---")
    print(f"Temperatura média do mês: {media:.2f}°C")
    print(f"Maior temperatura: {maior:.2f}°C")
    print(f"Menor temperatura: {menor:.2f}°C")
    print(f"Dias com temperatura acima de 27.3°C: {acima} dia(s)")

if __name__ == "__main__":
    main()
