"""
Exercício 038:
    Faça um programa que leia um vetor de 8 posições, e em seguinda, leia também dois valores X e Y quaisquer
correspondentes a duas posições no vetor. Ao final seu programa deverá escrever a soma dos valores encontrados nas
respectivas posições
"""
# Variáveis
vet = []
x, y = int(-1), int(-1)

# Entrada de dados
print("Digite 8 valores para o vetor:")
for cont in range(8):
    vet.append(int(input(f"Digite o valor para a posição {cont}: ")))

# Soma dos valores X e Y
while (x < 0 or x > 7) or (y < 0 or y > 7):

    x = int(input("\nDigite uma posição do vetor, de 0 a 7 para X: "))

    # Validação X
    if x < 0 or x > 7:
        print("Erro, digite números de 0 a 7 para X, tente novamente")

    y = int(input("Digite mais uma posição do vetor, de 0 a 7 para Y: "))

    # Validação Y
    if y < 0 or y > 7:
        print("Erro, digite números de 0 a 7 para Y, tente novamente")


soma = int(vet[x] + vet[y])

# Saída de dados
print(f"\nValor da posição X: {vet[x]}")
print(f"Valor da posição Y: {vet[y]}")
print(f"A soma dos valores da posição {x} e {y} é igual a: {soma}")
