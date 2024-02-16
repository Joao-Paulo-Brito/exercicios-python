"""
Exercício 037:
    Ler um conjunto de números reais, armazenar em um vetor e calcular o quadrado dos números desse vetor e adicionar em
outro vetor, de 10 elementos, depois imprimir os dois
"""
# Variáveis
vet = []
quadrado = []
mult = float(0)

# Entrada de dados
print("Digite 10 números reais")
for cont in range(1, 11):
    vet.append(input(f"Digite o {cont}° número: "))

# Cálculando o quadrado de cada valor
for cont in range(len(vet)):
    quadrado.append(float(vet[cont]) ** 2)  # ** é operação de potência, ou seja, elevado a 2

# Transformando em tupla, para os imutabilidade de dados
vet = tuple(vet)
quadrado = tuple(quadrado)

# Saída de dados
print("\nValores digitados:")
print(vet)
print("\nQuadrado dos valores:")
print(quadrado)
