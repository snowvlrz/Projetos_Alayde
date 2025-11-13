import random

# gerar vetor aleatório
def gerar_vetor(tamanho=25, minimo=1, maximo=100):
    return [random.randint(minimo, maximo) for _ in range(tamanho)]

# busca linear
def busca_linear(arr, alvo):
    """
    Retorna o índice da primeira ocorrência de 'alvo' em arr,
    ou -1 se não encontrado.
    """
    for i, val in enumerate(arr):
        if val == alvo:
            return i
    return -1

# selection sort
def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a

# insertion sort
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        chave = a[i]
        j = i - 1
        # desloca elementos maiores que chave para a direita
        while j >= 0 and a[j] > chave:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = chave
    return a

# busca binária iterativa
def busca_binaria(arr, alvo):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == alvo:
            return mid
        elif arr[mid] < alvo:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# demonstração
if __name__ == "__main__":
    # cria o vetor aleatório
    vetor = gerar_vetor(25, 1, 100)
    print("Vetor original (25 números):")
    print(vetor)
    print()

    # escolhe um alvo que com certeza existe: o primeiro elemento
    alvo_existe = vetor[0]
    # alvo que provavelmente não existe: -1 (fora do intervalo 1-100)
    alvo_nao_existe = -1

    # busca linear
    idx_linear = busca_linear(vetor, alvo_existe)
    print(f"Busca linear por {alvo_existe}: índice = {idx_linear} (deveria ser >= 0).")
    idx_linear_none = busca_linear(vetor, alvo_nao_existe)
    print(f"Busca linear por {alvo_nao_existe}: índice = {idx_linear_none} (deveria ser -1).")
    print()

    # ordena com selection sort e insertion sort
    sel_sorted = selection_sort(vetor)
    ins_sorted = insertion_sort(vetor)
    print("Selection sort resultado:")
    print(sel_sorted)
    print("Insertion sort resultado:")
    print(ins_sorted)
    print()

    # verificar se dão o mesmo resultado
    print("Selection == Insertion ? ->", sel_sorted == ins_sorted)
    print()

    # busca binária
    idx_binaria = busca_binaria(ins_sorted, alvo_existe)  # usando insertion sort (poderia usar selection também)
    print(f"Busca binária por {alvo_existe} na lista ordenada: índice = {idx_binaria}")
    # busca por algo que não existe
    idx_binaria_none = busca_binaria(ins_sorted, alvo_nao_existe)
    print(f"Busca binária por {alvo_nao_existe} na lista ordenada: índice = {idx_binaria_none} (deveria ser -1)")
