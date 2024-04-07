"""
    Exercícios de matrizes
    Exercício 1:
    Leia uma matriz 4x4 e escreva quantos valores maiores que 10 ela possui

matriz = []
counter = int(0)

# Entrada de dados
print("Digite elementos inteiros para a matriz:")
for i in range(4):
    linha = []

    for j in range(4):
        valor = int(input(f"Posição [{i}][{j}]: "))
        linha.append(valor)
        if valor > 10:
            counter += 1
        else:
            pass

    matriz.append(linha)
    print()

# Saída de dados
for line in matriz:
    print(line)

print(f"\nExistem {counter} valores maiores que 10\n")

    Exercício 2:
    Declare uma matriz 5x5, preencha com 1 a diagonal principal e com 0 o restate, escreva no final a matriz

# List compreesion da matriz
matriz = [[1 if coluna == linha else 0 for coluna in range(5)] for linha in range(5)]

# Saída de dados
for linha in matriz:
    print(linha)

    Exercício 3:
    Preencha uma matriz 5x5, sendo um desses elementos um "X", depois diga a posição da linha e da coluna desse elemeto,
caso o x não esteja na matriz, digite "X não encontrado"
matriz = []
posicao = None

print("Matriz 5x5")
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(input("Digite o elemento: "))
        if linha[j].lower() == "x":
            if posicao is not None:
                print("\nO X não pode ser digitado mais de uma vez\n")
                linha[j] = 0
            else:
                posicao = (i, j)

    print()
    matriz.append(linha)

# Saída de dados
for linha in matriz:
    print(linha)

if posicao is not None:
    print(f"\nO X está na posição: {posicao}")
else:
    print("\nO X não foi encontrado")

    Exercício 4:
    Leia uma matriz de 3x3 elementos. cada elemento do vetor terá o valor de 1 até 9 usando list comprehension.

elementos = [[coluna + 1 + linha * 3 for coluna in range(3)] for linha in range(3)]
for linha in elementos:
    print(linha)

    Exercício 5:
     Crie uma list comprehension que gere a sequência de Fibonacci até um determinado número n, mas inclua apenas os
números ímpares dessa sequência na lista resultante.

    Exercício 6:
    Use uma list comprehension para encontrar todos os números primos entre 2 e 50. Dica: Você pode precisar de uma
expressão aninhada ou uma função auxiliar.
"""
