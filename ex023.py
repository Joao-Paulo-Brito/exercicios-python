"""
Exercício 023:
    Faça um programa que receba dois número. Calcule e mostre:
    . A soma dos números pares desse intervalo de números, incluindo os números digitados
    . A multiplicação dos números impares desse intervalo de números, incluindo os digitados
"""
# Variáveis
soma = int(0)
multiplica = int(1)

# Entrada de dados
num1 = int(input("Digite um número inteiros: "))
num2 = int(input("Digite outro número inteiro: "))

for cont in range(num1, num2+1):

    # Somando os pares
    if cont % 2 == 0:
        soma += cont

    # Multiplicando os impares
    else:
        multiplica *= cont

print(f"\nA soma dos pares entre {num1} e {num2} é igual a: {soma}")
print(f"A multiplicação dos impares entre {num1} e {num2} é igual a: {multiplica}")
