"""
    Em matemática, o número harmónico designado por H é uma soma de série harmónica:
H(n) = 1+1/2+1/3+1/...+1/n

Faça um programa que leia o valor n inteiro e positivo e apresente o valor de H(n)
"""
# Variáveis
harmonico = float(0)
soma = float(0)

# Entrada de dados
print("\nValor harmónico\n")
n = int(input("Digite um valor inteiro e positivo para n: "))

# Cálculo
for cont in range(1, n + 1):
    soma += 1/cont
    harmonico = soma

# Saída de dados
print(f"O valor harmónico de n é {harmonico}")
