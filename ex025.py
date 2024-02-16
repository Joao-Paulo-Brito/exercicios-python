"""
Exercício 025:
    Escreva um programa que leia um número inteiro e cálcule a soma dos divisores de todos esses números, com excessão
dele próprio, ex: Número 66: 1+2+3+6+11+22+33 = 78
"""
# Variáveis
soma = int(0)

# Entrada de dados
numero = int(input("\nDigite um número para calcular a soma dos seus divisores: "))

# Soma
for cont in range(1, numero):
    if numero % cont == 0:
        soma += cont

# Saída de dados
print(f"\nA soma dos divisores de {numero} é igual a: {soma}")
