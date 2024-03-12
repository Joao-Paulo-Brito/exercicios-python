"""
    Exercício 047:
    Faça uma função com o parâmetro "numero", onde ela recebe um número para definir se é primo ou não, se for primo,
retorna True, caso contrário, retorna False
"""


def primo(numero):
    contador = int(0)

    for i in range(numero):
        if numero % (i+1) == 0:
            contador += 1

    if contador == 2:
        return True
    return False


# Entrada de dados
print("Verificando se o número é primo")
print("Número 8 ?", primo(8))
print("Número 3 ?", primo(3))
print("Número 7 ?", primo(7))
print("Número 10 ?", primo(10))
