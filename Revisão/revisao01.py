"""
Exercícios de revisão geral para revisar o conteúdo estudado em python:

1) Escreva um programa que verifique se um número é positivo, negativo ou zero.
    R=
# Entrada de dados
n = int(input("Digite um número qualquer: "))

# Verificação
if n > 0:
    print("\nO número é positivo")
elif n < 0:
    print("\nO número é negativo")
elif n == 0:
    print("\nO número é igual a 0")


2) Crie um programa que determine se um número é par ou ímpar.
    R=
# Entrada de dados
n = int(input("Digite um número qualquer: "))

# Validação
if not n % 2:
    print("\nO número é par")
else:
    print("\nO número é ímpar")


3) Faça um programa que verifique se um ano é bissexto.
    R=
# Entrada de dados
ano1 = [dia for dia in range(1, 366) if dia == 365]
ano2 = [dia for dia in range(1, 367) if dia == 366]

# Verificando
for listas in ano1, ano2:
    for dias in listas:
        print(f"Quantidade de dias: {dias}")
        if dias == 366:
            print("O ano é bissexto\n")
        else:
            print("O ano é normal\n")


4) Escreva um programa que classifique um triângulo em equilátero, isósceles ou escaleno.
    R=


# Função de verificação de dados
def triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado1 == lado3:
        return "O triângulo é equilatero"
    elif lado1 == lado2 and lado1 != lado3:
        return "O triângulo é isósceles"
    else:
        return "O triângulo é escaleno"


# Entrada de dados
print(triangulo(5, 5, 2))
print(triangulo(8, 8, 8))
print(triangulo(1, 2, 3))


5. Crie um programa que determine se um número é primo.
    R=

# Variáveis
primo = int()

# Entrada de dados
n = int(input("Digite um número qualquer: "))

for cont in range(n):
    if not cont % 2 and not n % cont:
        primo += 1
    else:
        pass

# Saída de dados
if primo == 2:
    print("\nO número é primo")
else:
    print("\nO número não é primo")


6) Faça um programa que compare duas strings e verifique se são palindromos
    R=


def palindromo(numero):
    numero = list(numero)
    numero.reverse()
    # Essa operação vai converter todos os números em strings, usando a função map(), depois junta os numeros em uma
    # string só, depois converte para inteiro.
    numero = int(''.join(map(str, numero)))
    if numero == int(n):
        return f"\nO número {numero} é palindromo"
    return f"\nO número {numero} não é palindromo"


print("Digite um número qualquer para verificar se é palindromo:")
n = input()

# Verificando
print(palindromo(n))


7) Escreva um programa que determine se uma pessoa pode votar ou não, baseado na idade.
    R=


def votacao(idade):
    if idade >= 18:
        return f"Você tem {idade} anos, já tem idade pra votar"
    return f"Você tem {idade} anos, você não pode votar"


# Entrada de dados
print(votacao(18))
print(votacao(10))
print(votacao(25))


8) Dada uma sequência de números inteiros informados pelo usuário (o usuário deve continuar inserindo números até que
ele decida parar), encontre o menor e o maior número da sequência sem usar funções prontas de min() e max() do Python.
    R=

# Variáveis
resposta = int(0)
maior = int(0)
menor = int(0)
numeros = []

# Loop
print("Digite números inteiros, para saber qual é o maior e o menor")
print("Caso queira parar, digite 1")
while resposta != 1:
    resposta = int(input("\nDigite um número: "))
    if resposta != 1:
        numeros.append(resposta)

    if resposta > maior:
        maior = resposta

    if resposta < menor and resposta != 1:
        menor = resposta
    elif menor == 0 and len(numeros) == 1:
        menor = resposta

# Saída de dados
print(f"\nNumeros digitados: {numeros}")
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")


9. Faça um programa que calcule a soma dos números de 1 a 100.
10. Escreva um programa que imprima os números primos de 1 a 100.
11. Crie um programa que ordene uma lista de números.
12. Escreva uma função que inverta uma string.
13. Escreva um programa que imprima os primeiros 20 termos da sequência de Fibonacci.
14. Faça um programa que imprima os números pares de 0 a 100.
15. Crie um programa que calcule o fatorial de um número.
16. Escreva um programa que imprima os números de 1 a 10.
17. Escreva uma função que calcule o quadrado de um número.
18. Faça uma função que receba **kwargs e imprima cada chave e valor.
19. Escreva uma função que determine se um número é positivo, negativo ou zero.
20. Crie uma função que receba um número variável de argumentos e retorne o maior deles.
Escreva uma list comprehension que gere os quadrados dos números de 1 a 10.
Crie uma dictionary comprehension que mapeie os números de 1 a 10 para seus respectivos quadrados.
Faça uma set comprehension que filtre os números pares de 1 a 20.
Escreva uma list comprehension que gere uma lista com as vogais de uma string.
Escreva um programa que crie uma lista com os números de 1 a 10.
Crie um programa que verifique se um elemento está presente em uma lista.
Faça um programa que remova os elementos repetidos de uma lista.
Escreva um programa que some todos os elementos de uma lista.
Escreva um programa que imprima a tabuada de um número escolhido pelo usuário.
Faça um programa que imprima a série de Fibonacci até que o valor seja maior que 1000.
Escreva uma função que receba uma lista de números e retorne a média.
Faça uma função que verifique se uma palavra é um palíndromo.
Crie um programa que converta uma lista de números para uma tupla.
Escreva um programa que conte a frequência de cada elemento em uma lista.
Crie um programa que inverta uma lista.
Crie uma dictionary comprehension que conte a frequência de cada letra em uma string.
Escreva um programa que solicite ao usuário uma sequência de números separados por vírgula e crie uma lista com esses
números.
Crie uma função que receba duas listas como parâmetros e retorne uma nova lista contendo apenas os elementos comuns
entre as duas listas.
Faça um programa que leia uma frase do usuário e conte quantas palavras diferentes existem na frase.
Escreva um programa que simule o lançamento de um dado de seis lados, imprimindo o resultado obtido.
"""
