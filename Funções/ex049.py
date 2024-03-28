"""
    Exercício 049:
    Faça funções que criem formas geometricas, como um retângulo e um quadrado, usando uma dupla de for
"""


def quadrado(lado):

    for linha in range(lado):

        for coluna in range(lado):
            if coluna+1 < lado:
                print(" * ", end="")
            else:
                print(" * ", end="\n")
    print("\n")


def triangulo(lado):
    # Para cada linha do triângulo
    for cont in range(1, lado + 1):
        # Calcula a quantidade de asteriscos na linha. Cada linha tem um número ímpar de asteriscos.
        num_asteriscos = 2 * cont - 1
        # Calcula a quantidade de espaços em branco antes do primeiro asterisco na linha
        espacos = lado - cont
        # Imprime os espaços em branco
        print(' ' * espacos, end='')
        # Imprime os asteriscos
        print('*' * num_asteriscos)


# Quadrados
quadrado(2)
quadrado(6)

# Triangulos
triangulo(5)
