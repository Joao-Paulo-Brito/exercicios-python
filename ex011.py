"""
Exercício 011:
    Ler um número inteiro, se o número for negativo, imprima opção inválida, se for positivo, calcule o logaritimo desse
número.
"""
import math


# Entrada de dados
print("\nCálculo de logaritmo\n")
numero = int(input("Digite qualquer número inteiro maior que 0: "))

# Condição
if numero < 0:
    print("Opção inválida, tente novamente")
else:
    # Cálculo de logaritmo de base 10
    log = round(float(math.log10(numero)), 2)

    # Saída de dados
    print(f"\nO logaritmo do número {numero} é igual a {log}")
