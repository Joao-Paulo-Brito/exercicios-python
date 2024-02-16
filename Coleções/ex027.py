"""
Exercício 027:
    Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
# Varíaveis
numeros = []

# Entrada de dados
print("Digite 5 números: ")
for cont in range(1, 5+1):
    n = int(input())
    numeros.append(n)

# Saída de dados
print(numeros)
