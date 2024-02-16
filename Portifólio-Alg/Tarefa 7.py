import timeit


# Função soma_iterativa
def soma_iterativa(n, a):
    s = 0
    for i in range(n):
        s += a[i]
    return s


def main():
    # Variáveis
    n1 = 2500
    n2 = 2900

    # Construindo o vetor a com elementos de 1 a n
    a1 = list(range(1, n1 + 1))
    a2 = list(range(1, n2 + 1))

    # Medindo o tempo de execução para n = 2500
    tempo_execucao1 = timeit.timeit(lambda: soma_iterativa(n1, a1), number=1000)

    # Medindo o tempo de execução para n = 2900
    tempo_execucao2 = timeit.timeit(lambda: soma_iterativa(n2, a2), number=1000)

    # Exibindo resultados parciais e tempo de execução
    print(f"Resultado para n = {n1}: {soma_iterativa(n1, a1)}")
    print(f"Tempo de execução para n = {n1}: {tempo_execucao1:.4f} segundos")

    print(f"\nResultado para n = {n2}: {soma_iterativa(n2, a2)}")
    print(f"Tempo de execução para n = {n2}: {tempo_execucao2:.4f} segundos")


if __name__ == "__main__":
    main()
