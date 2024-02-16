# Importação da biblioteca "timeit"
import timeit


# Função "Soma_Quadrados A"
def soma_quadrados_a(n):
    x = 0
    for j in range(1, n + 1):
        x = x + j * j
    return x


# Entrada de dados:
n = int(input("Digite um limite para a soma dos quadrados: "))

# Biblioteca timeit para medir o tempo de execução com mais precisão
tempo_execucao_a = round(timeit.timeit(lambda: soma_quadrados_a(n), number=10000), 4)

# Resultado da função A
resultado_a = soma_quadrados_a(n)

# Saída de dados Função A
print(f"\nA soma dos quadrados de 1 até {n} usando a função A é {resultado_a}")
print(f"Tempo de execução (Função A): {tempo_execucao_a} segundos\n")
