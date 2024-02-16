import timeit
import sys

# Aumentar o limite de recursão
sys.setrecursionlimit(10000)


# Implementação recursiva de F(n)
def recursivo_f(n, f0):
    if n == 0:
        return f0
    return recursivo_f(n - 1, f0) + n + 1


# Implementação de F(n) com a fórmula fechada
def formula_f(n, f0):
    return (n * (n + 1) + 2 * (n + f0)) // 2


valores_n = [100, 1000]
valores_f0 = [1, 10]

for n in valores_n:
    for f0 in valores_f0:
        if n <= 1000:
            tempo_recursivo = timeit.timeit(lambda: recursivo_f(n, f0), number=1000)
            print(f"Recursivo: F({n}, {f0}) = {recursivo_f(n, f0)}")
            print(f"Tempo de Execução: {tempo_recursivo:.4f} segundos")

        tempo_formula = timeit.timeit(lambda: formula_f(n, f0), number=1000)
        print(f"\nFórmula Fechada: F({n}, {f0}) = {formula_f(n, f0)}")
        print(f"Tempo de Execução: {tempo_formula:.4f} segundos\n")
