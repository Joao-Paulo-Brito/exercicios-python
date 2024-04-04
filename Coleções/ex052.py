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
"""
matriz = []
posicao = []
cont = int(0)

print("Matriz 5x5")
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(input("Digite o elemento: "))
        if cont > 0:
            print("\nNão pode digitar o x mais de uma vez!\n")
            break
        elif "x" in linha:
            posicao.append(i, j)
            cont += 1

    matriz.append(linha)

for lista in matriz:
    for numero in lista:
        if numero.lower() == "x":
            print(f"X encontrado ! está na posição: {posicao}")

