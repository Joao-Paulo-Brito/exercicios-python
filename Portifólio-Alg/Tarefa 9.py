import timeit


# Função iterativa
def max_i(a, n):
    x = a[0]
    for i in range(1, n):
        if a[i] > x:
            x = a[i]
    return x


# Função recursiva
def max_r(a, n):
    if n == 1:
        return a[0]
    else:
        x = max_r(a, n - 1)
        if x < a[n - 1]:
            return a[n - 1]
        else:
            return x


# n=10
n1 = 10
a1 = list(range(1, n1 + 1))

print("\n------------------------------n=10--------------------------------------")
tempo_1_max_i = round(timeit.timeit(lambda: max_i(a1, n1), number=1000), 6)
print(f"Tempo médio de execução da função Max-I: {tempo_1_max_i} segundos")

tempo_1_max_r = round(timeit.timeit(lambda: max_r(a1, n1), number=1000), 6)
print(f"Tempo médio de execução da função Max-R: {tempo_1_max_r} segundos")
print("------------------------------------------------------------------------\n")

# n=100
n2 = 100
a2 = list(range(1, n2 + 1))

print("-----------------------------n=100--------------------------------------")
tempo_2_max_i = round(timeit.timeit(lambda: max_i(a2, n2), number=1000), 6)
print(f"Tempo médio de execução Max-I (n={n2}): {tempo_2_max_i} segundos")

tempo_2_max_r = round(timeit.timeit(lambda: max_r(a2, n2), number=1000), 6)
print(f"Tempo médio de execução Max-R (n={n2}): {tempo_2_max_r} segundos")
print("------------------------------------------------------------------------\n")
