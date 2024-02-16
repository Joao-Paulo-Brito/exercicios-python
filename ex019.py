"""
Exercício 019:
    Faça um programa que peça 10 números, usando for, para o usuário e some todos.
"""
# Variáveis
soma = int(0)

# Entrada de dados
for cont in range(1, 11):
    resposta = int(input(f"Digite o {cont}° número: "))

    # Somando
    soma = soma + resposta

# Saída de dados
print(f"\nA soma de todos esses números é {soma}")
