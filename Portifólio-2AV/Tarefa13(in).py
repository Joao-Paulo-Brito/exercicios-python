import timeit


def fib_recursivo(n):
    if n >= 2:
        return fib_recursivo(n - 1) + fib_recursivo(n - 2)
    else:
        return n


def fib_iterativo(n):
    cont, atual, ultimo, penultimo = int(1), int(0), int(0), int(1)
    while cont <= n:
        atual = ultimo + penultimo
        penultimo = ultimo
        ultimo = atual
        cont += 1
    return atual


# Entrada de dados
n = int(input("Digite um valor para o exibir a sequência de fibornacci: "))

# Medição para a versão recursiva
tempo_recursivo = timeit.timeit(lambda: fib_recursivo(n), number=1)

# Medição para a versão iterativa
tempo_iterativo = timeit.timeit(lambda: fib_iterativo(n), number=1)

# Valores
resultado_recursivo = fib_recursivo(n)
resultado_iterativo = fib_iterativo(n)

# Saída de dados
print(f"Usando recursão: Fibonacci({n}) = {resultado_recursivo}")
print(f"Tempo de execução recursivo: {tempo_recursivo:.6f}\n")
print(f"Usando iteração: Fibonacci({n}) = {resultado_iterativo}")
print(f"Tempo de execução iterativo: {tempo_iterativo:.6f}\n")
print("Memória RAM do computador: 16GB")
