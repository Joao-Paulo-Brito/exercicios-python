"""
Exercício 041:
    Faça um programa que leia um vetor de 10 posições, atribua o valor 0 para a posição do vetor que tiver valor
negativo, e depois leia um valor x e mostre os multiplos desse número do vetor que foi criado.
"""
# Variáveis
vet = []
multiplos = []

# Entrada de dados
print("Digite 10 valores: ")
for cont in range(10):
    vet.append(int(input(f"Digite o {cont+1}° valor: ")))

    # Atribuindo o valor 0
    if vet[cont] < 0:
        vet[cont] = 0

# Valor x
print("\nDigite um valor para X:")
x = int(input())

# Multiplos de x
for valor in vet:
    if valor % x == 0:
        multiplos.append(valor)

# Saída de dados
print(f"Valores do vetor: {vet}")
print(f"Valores do vetor que são múltiplos de x({x}): {multiplos}")
