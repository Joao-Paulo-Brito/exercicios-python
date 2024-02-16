import timeit


# Função Soma-Dir-Esq
def soma_dir_esq(n, a):
    s = 0
    for k in range(n, 0, -1):
        s += a[k - 1]
    return s


# Função Soma-Esq-Dir
def soma_esq_dir(n, a):
    s = 0
    for k in range(n):
        s += a[k]
    return s


# Função para criar uma lista a com elementos de 1 a n
def criar_lista(n):
    return list(range(1, n + 1))


# Números de n para o teste
n1 = 2500
n2 = 2900

# Criar listas com elementos de 1 a n
a1 = criar_lista(n1)
a2 = criar_lista(n2)

# Medir o tempo de execução da Soma-Dir-Esq para n1 e n2 usando timeit
tempo1 = round(timeit.timeit(lambda: soma_dir_esq(n1, a1), number=1000), 3)
tempo2 = round(timeit.timeit(lambda: soma_dir_esq(n2, a2), number=1000), 3)

# Saída de dados
print("\n--------------------Soma direita para esquerda---------------------")
print(f"Resultado da Soma-Dir-Esq para n1 = {n1}: {soma_dir_esq(n1, a1)}")
print(f"Resultado da Soma-Dir-Esq para n2 = {n2}: {soma_dir_esq(n2, a2)}")
print(f"Tempo de execução médio da Soma-Dir-Esq: {tempo1} segundos para n1")
print(f"Tempo de execução médio da Soma-Dir-Esq: {tempo2} segundos para n2")
print("-------------------------------------------------------------------")

# Medir o tempo de execução da Soma-Esq-Dir para n1 e n2 usando timeit
tempo1 = round(timeit.timeit(lambda: soma_esq_dir(n1, a1), number=1000), 3)
tempo2 = round(timeit.timeit(lambda: soma_esq_dir(n2, a2), number=1000), 3)

print("\n--------------------Soma esquerda para direita---------------------")
print(f"\nResultado da Soma-Esq-Dir para n1 = {n1}: {soma_esq_dir(n1, a1)}")
print(f"Resultado da Soma-Esq-Dir para n2 = {n2}: {soma_esq_dir(n2, a2)}")
print(f"Tempo de execução médio da Soma-Esq-Dir: {tempo1} segundos para n1")
print(f"Tempo de execução médio da Soma-Dir-Esq: {tempo2} segundos para n2")
print("-------------------------------------------------------------------")
