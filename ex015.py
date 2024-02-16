"""
Exercício 015:
    Escreva um programa que calcule a soma de todos os números pares de 1 a N, onde N é um número inteiro fornecido pelo
usuário, use o loop for.
"""
# Variáveis
soma = int(0)

# Entrada de dados
n = int(input("\nDigite um número limite para o cálculo de seus antecessores pares: "))

# Soma dos pares
for cont in range(1, n+1):
    if cont % 2 == 0:
        soma += cont

# Saída de dados
print(f"A soma dos números pares até {n} é igual a: {soma}")
