"""
Exercício 044:
    Faça uma função que receba uma lista e exiba os elementos da última metade na frente dos elementos da primeira
metade.
"""


def metade():
    lista2 = []

    for cont2 in range(len(lista)):
        if cont2+1 > len(lista)/2:
            lista2.append(lista[cont2])

    for cont2 in range(len(lista)):
        if cont2+1 <= len(lista)/2:
            lista2.append(lista[cont2])

    return lista2


# Variáveis
lista = []

# Entrada de dados
print("Digite o tamanho da lista de elementos que você quer: ")
tamanho = int(input())

for cont in range(tamanho):
    lista.append(input(f"Digite o {cont+1}° elemento: "))

# Saída de dados
print(f"\nInvertendo ordem da lista: {metade()}")
