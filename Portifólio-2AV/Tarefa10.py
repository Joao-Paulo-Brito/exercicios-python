import timeit


# Algoritmo Iterativo
def decide_iterativo(a, n, x):
    for i in range(n):
        if a[i] == x:
            return "SIM"
    return "NÃO"


# Algoritmo Recursivo
def decide_recursivo(a, n, x):
    if n == 0:
        return "NÃO"
    if a[n - 1] == x:
        return "SIM"
    return decide_recursivo(a, n - 1, x)


# Função para criar o vetor a[1 .. n]
def vetor(n):
    return list(range(1, n + 1))


# Solicitar entrada do usuário para n e x
n = int(input("Digite o valor de n: "))
x = int(input(f"Digite o valor de x (entre 1 e {n}): "))

# Verificar se o valor de x está dentro do intervalo
if x < 1 or x > n:
    print("\nO valor de x está fora do intervalo permitido.")
else:
    a = vetor(n)

    # Medir o tempo para o algoritmo iterativo
    tempo_iterativo = round(timeit.timeit(lambda: decide_iterativo(a, n, x), number=10000), 3)

    # Medir o tempo para o algoritmo recursivo
    tempo_recursivo = round(timeit.timeit(lambda: decide_recursivo(a, n, x), number=10000), 3)

    print(f"\nn = {n}")
    print(f"Resultado Iterativo: {decide_iterativo(a, n, x)}")
    print(f"Tempo Iterativo: {tempo_iterativo} segundos\n")

    print(f"Resultado Recursivo: {decide_recursivo(a, n, x)}")
    print(f"Tempo Recursivo: {tempo_recursivo} segundos\n")
