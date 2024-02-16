"""
Exercício 020:
    Escreva um programa usando while onde peça para o usuário digitar 10 números, depois mostrar o menor valor lido e o
maior valor lido
"""
# Variáveis
cont = int(0)
menor = int(0)
maior = int(0)

# Entrada de dados
while cont < 10:
    cont += 1
    resposta = int(input(f"Digite o {cont}° número: "))

    # Menor valor
    if menor == 0:
        menor = resposta
    else:
        if resposta < menor:
            menor = resposta

    # Maior valor
    if resposta > maior:
        maior = resposta

# Saída de dados
print(f"\nO menor valor é {menor}, e o maior valor é {maior}")
