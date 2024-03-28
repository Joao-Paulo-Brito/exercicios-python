"""
    Exercício 050:
    Escreva uma função que receba um número inteiro e retorne a soma dos quadrados dos seus dígitos.
"""


def digitos_quadrados(numero):
    quadrados = [int(digito) for digito in str(numero)]  # List compression

    for cont in range(len(quadrados)):
        quadrados[cont] = quadrados[cont] ** 2

    return f"A soma dos quadrados: {quadrados} é {sum(quadrados)}"


print(digitos_quadrados(556))
