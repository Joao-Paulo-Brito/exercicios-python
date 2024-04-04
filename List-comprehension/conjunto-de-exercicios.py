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

    Exercício 4:
    Use list comprehension para criar uma lista de tuplas (x, y) onde x é um número ímpar de 1 a 10 e y é um número par
de 1 a 10.
R =
pares = tuple([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if not x % 2])
impares = tuple([y for y in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if y % 2])
print(f"Pares: {pares}")
print(f"Ímpares: {impares}")
----------------------------REFATORANDO-------------------------------
"""
pares_impares = [(x, y) for x in range(1, 11) for y in range(1, 11) if x % 2 == 0 and y % 2 != 0]
par = [numero for pares in pares_impares for numero in pares if numero % 2 == 0 and numero != numero]
print(par)
