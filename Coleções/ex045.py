"""
    Exercício 045:
    Desenvolva uma função eh_palindromo que recebe uma string e retorna True se a string for um palíndromo e False caso
contrário. Um palíndromo é uma palavra que tem a mesma sequência de caracteres tanto da esquerda para a direita quanto
da direita para a esquerda.
"""


def eh_palindromo():
    palavras = list(sequencia)
    inverso = palavras.copy()  # Deep copy
    inverso.reverse()

    if palavras == inverso:
        return True
    return False


# Entrada de dados
print("-"*20+"Teste de Palindromo"+"-"*20)
sequencia = str(input("Digite uma sequência de caracteres: "))

# Saída de dados
print(f"\nA sequência: '{sequencia}' é palindrome ?")
print(eh_palindromo())
