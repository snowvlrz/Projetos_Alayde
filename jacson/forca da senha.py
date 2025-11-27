import string

def verificar_senha(senha):
    regras_falhas = []

    # regra comprimento
    if len(senha) < 8:
        regras_falhas.append("mínimo de 8 caracteres")

    # maiúsculas
    if not any(c.isupper() for c in senha):
        regras_falhas.append("pelo menos 1 letra maiúscula")

    # minúsculas
    if not any(c.islower() for c in senha):
        regras_falhas.append("pelo menos 1 letra minúscula")

    # dígitos
    if not any(c.isdigit() for c in senha):
        regras_falhas.append("pelo menos 1 número")

    # caractere especial (usa string.punctuation)
    especiais = set(string.punctuation)
    if not any(c in especiais for c in senha):
        regras_falhas.append("pelo menos 1 caractere especial (ex: !@#$%&*)")

    return regras_falhas

def main():
    senha = input("Digite a senha: ")
    falhas = verificar_senha(senha)
    if not falhas:
        print("Senha definida: FORTE ✅")
    else:
        print("Senha: FRACA ❌")
        print("Regras não cumpridas:")
        for r in falhas:
            print(f"- {r}")

if __name__ == "__main__":
    main()
