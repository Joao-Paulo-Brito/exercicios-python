"""
Exercício 021:
    Escreva um programa que detecte se um número é primo ou não
"""
# Variáveis
cont = int(0)
primo = int(0)

# Entrada de dados
print("\nDigite um número para detectar se é primo ou não: ")
numero = int(input())

# Detectando
while cont < numero:
    cont += 1
    if cont == 1 or cont == numero:

        # Variável "primo" ganha um ponto
        if numero % cont == 0:
            primo += 1

    elif cont != 1 or cont != numero:

        # Variável "primo" perde um ponto
        if numero % cont == 0:
            primo -= 1

if primo == 2:
    print(f"O número {numero} é primo")
else:
    print(f"O número {numero} não é primo")
