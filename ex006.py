"""
Exercício 006:
    Com base na tabela abaixo, escreva um programa que leia o código do item e a quantidade desse item. Depois calcule
o preço total:
--------------------------------------
|| Código || Especificação || preço ||
--------------------------------------
||   1    ||Cachorro Quente|| R$4,00||
||   2    ||    X-Salada   || R$4,50||
||   3    ||    X-Bacon    || R$5,00||
||   4    ||Torrada Simples|| R$2,00||
||   5    ||  Refrigerante || R$1,50||
--------------------------------------
Exemplo:
Código: 3
Quantidade: 2
Total a pagar: R$10,00
"""

# Entrada de dados
print("Leia a tabela a baixo e digite o código do item e a sua quantidade:")
print("--------------------------------------")
print("|| Código || Especificação || preço ||")
print("--------------------------------------")
print("||   1    ||Cachorro Quente|| R$4,00||")
print("||   2    ||    X-Salada   || R$4,50||")
print("||   3    ||    X-Bacon    || R$5,00||")
print("||   4    ||Torrada Simples|| R$2,00||")
print("||   5    ||  Refrigerante || R$1,50||")
print("--------------------------------------")

codigo = int(input("Digite o código do item: "))

quantidade = int(input("Digite a quantidade desse item: "))

if codigo == 1:
    preco = round(float(quantidade*4), 3)
elif codigo == 2:
    preco = round(float(quantidade*4.5), 3)
elif codigo == 3:
    preco = round(float(quantidade*5), 3)
elif codigo == 4:
    preco = round(float(quantidade*2), 3)
elif codigo == 5:
    preco = round(float(quantidade*1.5), 3)
else:
    print("Error, opção inválida de código")

# Saída de dados
print(f"O preço total a se pagar é: R${preco}")
