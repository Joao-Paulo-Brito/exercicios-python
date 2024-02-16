"""
Exercício 017:
    Escreva um programa que escreva na tela, de 1 até 100 3 vezes, a primeira contagem é usando for, a segunda usando
while, e a terceira usando do while
"""
# Loop for
print("\nLoop for: ")
for cont in range(1, 100+1):
    print(cont)

contador = int(0)
# While
print("\nLoop while: ")
while contador < 100:
    contador += 1
    print(contador)

contador = int(0)
# Do while
print("\nLoop Do While: ")
while True:
    contador += 1
    if contador <= 100:
        print(contador)
    else:
        break
