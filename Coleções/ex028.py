"""
Exercício 028:
    Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
# Entrada de dados
print("Digite 10 números reais:")
vetor = []

# Colocando números digitados no vetor
for cont in range(1, 10+1):
    numeros = float(input())
    vetor.append(numeros)

# Invertedo lista
vetor.reverse()

# Saída de dados
print("\nInvertendo lista...\n")
print(vetor)
