"""
Exercício 016:
    Faça um programa que determine e mostre os 5 primeiros múltiplos de 3, considerando números maiores que 0.
"""
# Variáveis
cont = int(0)
multiplos = int(0)

print("\n5 primeiros multiplos de 3: ")
while cont < 5:
    multiplos += 1
    if multiplos % 3 == 0:
        cont += 1
        print(multiplos)
