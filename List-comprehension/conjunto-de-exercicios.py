"""
    Exercício 1:
    Converter Temperaturas: Dada uma lista de temperaturas em Celsius, converta-as para Fahrenheit usando list
comprehension. A fórmula para a conversão é (9/5) * Celsius + 32.
    R =
temperaturas_celsius = [22, 34, 15, 27]
temperatuas_fahrenheit = [(9/5) * temperatura + 32 for temperatura in temperaturas_celsius]
print(temperatuas_fahrenheit)

    Exercício 2:
    Filtrar Palavras: Dada uma lista de palavras, use list comprehension para criar uma nova lista contendo apenas as
palavras que têm mais de 4 letras e mostre em letra maíuscula.
    R =
palavras = ["king", "jin", "kazuya", "law", "eddy", "yoshimitsu", "heihachi", "nina"]
filtro = [palavra.title() for palavra in palavras if len(palavra) <= 4]
print(filtro)

    Exercício 3:
    Considere uma matriz (lista de listas) matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]. Use list comprehension para
achatar essa matriz em uma única lista que contém todos os elementos da matriz.
    R=
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista = [numero for lista in matriz for numero in lista]
print(lista)

    Exercício 4:
    Use list comprehension para criar uma lista de tuplas (x, y) onde x é um número ímpar de 1 a 10 e y é um número par
de 1 a 10.
    R =
pares = tuple([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if not x % 2])
impares = tuple([y for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if y % 2])
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
#OBS: 1 = True, 0 = False
----------------------------REFATORANDO-------------------------------
# A função zip() serve para juntar em uma tupla, elementos de duas ou mais listas
pares = [x for x in range(1, 11) if x % 2 == 0]
impares = [y for y in range(1, 11) if y % 2]
lista = list(zip(pares, impares))
print(lista)

    Exercício 5:
    Dado um dicionário alunos = {'João': 15, 'Maria': 17, 'Pedro': 16, 'Ana': 18}, crie um novo dicionário onde as
chaves são os nomes dos alunos e os valores são True se o aluno for maior de idade (idade >= 18) e False caso contrário.
    R=
alunos = {'João': 15, 'Maria': 17, 'Pedro': 16, 'Ana': 18}
maioridade = {aluno: True if idade >= 18 else False for aluno, idade in alunos.items()}
print(maioridade)

    Exercício 6:
    Crie um dicionário onde as chaves são os números de 1 a 10 e os valores são True se o número for par e False caso
contrário.
    R=
numeros = {chave: True if chave % 2 == 0 else False for chave in range(1, 11)}
print(numeros)

    Exercício 7:
    Dada uma lista de palavras, crie um dicionário onde as chaves são as palavras e os valores são o comprimento dessas
palavras.
    R =
palavras = ["Pão", "açucar", "pimenta", "tomate", "abobora", "pepino", "café"]
comprimento = {chave: valor for chave in palavras for valor in range(len(chave)+1)}
print(comprimento)

    Exercício 8:
    Dada uma lista de números, crie um dicionário onde as chaves são os números e os valores são True se o número for
primo e False caso contrário.

    Exercício 9:
    Dada uma lista de strings, crie um dicionário onde as chaves são as palavras e os valores são o número de
ocorrências dessa palavra na lista.

    Exercício 10:
    Dado um dicionário onde as chaves são nomes de produtos e os valores são seus preços, crie um novo dicionário onde
as chaves são os nomes dos produtos com desconto de 10% e os valores são os preços com desconto aplicado.

    Exercício 11:
    Dada uma lista de tuplas representando pares (chave, valor), crie um dicionário a partir desses pares.
"""

