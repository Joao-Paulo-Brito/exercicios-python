"""
Exercício 024:
    Faça um programa que leia números positívos e imprima seus divisores
"""
# Entrada de dados
print("Digite um número positivo: ")
numero = int(input())

print(f"Divisores anteriores de {numero}")
for cont in range(1, numero):

    # Saída de dados
    if numero % cont == 0:
        print(cont)
