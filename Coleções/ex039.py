"""
Exercício 039:
    Faça um vetor onde o usuário vai digitar o tamanho do vetor, os valores, e depois mostre os valores pares, o maior
valor, o menor valor e a soma de todos os valores.
"""
# Variáveis
vetor = []
pares = []

# Entrada de dados
print("Digite o tamnaho do vetor: ")
tamanho = int(input())

for cont in range(tamanho):
    vetor.append(int(input(f"Digite o {cont+1}° valor: ")))

    # Valores pares
    if vetor[cont] % 2 == 0:
        pares.append(int(vetor[cont]))

# Saída de dados
print(f"\nValores do vetor: {vetor}")
print(f"Valores pares: {pares}")
print(f"Maior valor: {max(vetor)}")
print(f"Menor valor: {min(vetor)}")
print(f"Soma dos valores: {sum(vetor)}")
