"""
Exercício 035:
    Faça um programa que possua um determinado valor A que armazene 6 números inteiros. O programa deve executar
os seguintes passos:
    (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
    (b) Armazene em uma variável inteira(simples) a soma entre os valores das posições A[0], A[1], A[5] do vetor e
    mostre na tela a sua soma
    (c) Modifique o veto na posição 4, atribuindo a esta posição o valor 100.
    (d) Mostre na tela cada valor do vetor A, um em cada linha.
"""
# Variáveis
A = [1, 0, 5, -2, -5, 7]
# Type Hint
soma: int

# Soma dos valores
print("Soma de 1 + 0 + 7")
soma = int(A[0] + A[1] + A[5])
print(soma)

# Posição 4 recebe 100
A[4] = 100

# Mostrar na tela os valores de A, por cada linha
print("\nNovos valores de A")
for cont in range(len(A)):
    print(A[cont])
