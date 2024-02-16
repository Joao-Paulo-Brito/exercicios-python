import sys


def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]
    s = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i - 1][j - 1] = sys.maxsize

            for k in range(i, j):
                q = m[i - 1][k - 1] + m[k][j - 1] + p[i - 1] * p[k] * p[j]
                if q < m[i - 1][j - 1]:
                    m[i - 1][j - 1] = q
                    s[i - 1][j - 1] = k

    return m, s


def print_optimal_parentheses(s, i, j, matrix_name):
    if i == j:
        print(f'M{matrix_name}[{i},{j}]', end="")
    else:
        print("(", end="")
        print_optimal_parentheses(s, i, s[i - 1][j - 1], matrix_name)
        print_optimal_parentheses(s, s[i - 1][j - 1] + 1, j, matrix_name)
        print(")", end="")


def main():
    n = int(input("Número de matrizes n: "))
    dimensions = []

    print("Digite as dimensões das matrizes:")
    for i in range(n + 1):
        dimensions.append(int(input(f'Dimensão da matriz M{i}: ')))

    m, s = matrix_chain_order(dimensions)

    print("\nTabela de dados calculados pela programação dinâmica para o produto:")
    for i in range(n):
        for j in range(n):
            print(f"m{i + 1}{j + 1}={m[i][j]}", end="  ")
        print()

    for i in range(1, n + 1):
        print(f'\nSolução ótima para M{i}:')
        print_optimal_parentheses(s, 1, i, i)
        print()


if __name__ == "__main__":
    main()
