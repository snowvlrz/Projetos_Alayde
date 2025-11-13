# busca por selection sort (ordenação)
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


# busca depois da ordenação
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


# vetor exemplo
vetor = [37, 6, 62, 64, 2, 70, 8, 60, 45, 39, 99, 64, 52, 74, 25, 55, 11, 91, 2, 95, 3, 51, 19, 29, 94]

print("Vetor original (25 números):")
print(vetor)
print()

# selection sort
ordenado = selection_sort(vetor)
print("Vetor ordenado (Selection Sort):")
print(ordenado)
print()

# busca depois da ordenação
alvo_existe = 37
alvo_nao_existe = -1

idx_binaria = busca_binaria(ordenado, alvo_existe)
print(f"Busca binária por {alvo_existe} na lista ordenada: índice = {idx_binaria}")
idx_binaria_none = busca_binaria(ordenado, alvo_nao_existe)
print(f"Busca binária por {alvo_nao_existe} na lista ordenada: índice = {idx_binaria_none} (deveria ser -1)")
