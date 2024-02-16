# Importação da biblioteca "timeit"
import timeit


# Função "Soma_Quadrados B"
def soma_quadrados_b(n):
    x = (n*(n+1)*(2*n+1))//6
    return x


# Entrada de dados:
n = int(input("Digite um limite para a soma dos quadrados: "))

# Biblioteca timeit para medir o tempo de execução com mais precisão
tempo_execucao_b = round(timeit.timeit(lambda: soma_quadrados_b(n), number=10000), 4)

# Resultado da função B
resultado_b = soma_quadrados_b(n)

# Saída de dados Função B
print(f"\nA soma dos quadrados de 1 até {n} usando a função B é {resultado_b}")
print(f"Tempo de execução (Função B): {tempo_execucao_b} segundos\n")
