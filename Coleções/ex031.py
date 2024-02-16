"""
Exercício 031:
    Crie uma lista para frutas, com maçã, banana e morango, depois de criar, adicione uva na lista, depois crie mais uma
lista chamada "frutas-extras" e coloque açaí e abacaxi, depois junte essa lista na lista original de frutas, depois
adicione laranja na posição 2 da lista de frutas, remova a banana da lista, depois remova o último elemento da lista de
frutas e adicione a uma nova lista, chamada de "frutas-removidas", depois imprima essas duas listas.
"""
# Entrada de dados
frutas = ['maçã', 'banana', 'morango']

# Adicionando uva
frutas.append('uva')

# Frutas extras
frutas_extras = ['açaí', 'abacaxi']
frutas.extend(frutas_extras)

frutas.insert(2, 'laranja')

# Removendo frutas
frutas.remove('banana')

frutas_removidas = [frutas.pop()]

print(frutas)
print(frutas_extras)
print(frutas_removidas)
