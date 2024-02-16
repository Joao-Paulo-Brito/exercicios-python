"""
Exercício 022:
    Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""
# Variáveis
soma = int(0)

# Entrada de dados
print("Digite um limite para a soma dos números pares: ")
limite = int(input())

# Somando
for cont in range(1, limite+1):
    if cont % 2 == 0:
        soma += cont

print(f"\nA soma dos números pares é : {soma}")
