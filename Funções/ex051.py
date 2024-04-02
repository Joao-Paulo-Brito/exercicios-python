"""
    Exercício 051:
    Faça uma função que calcula o número de fibonacci até o n-éssimo termo, e mostre na tela
"""


def fibonacci(n):
    numeros = [0]
    cont = int(1)
    soma = int(1)

    while soma < n:
        if n == 0:
            return numeros
        else:
            numeros.append(soma)
            soma = numeros[cont] + numeros[cont-1]
            cont += 1

    return numeros


print(fibonacci(15))
