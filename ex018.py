"""
Exercício 018:
    Faça um programa usando while que mostra uma contagem regressiva de 10 até 0, mostrando a mensagem "fim" depois
"""
# Contagem regressiva
contador = int(10)

print("\nIniciando contagem regressiva")

while contador >= 0:
    print(contador)
    contador -= 1
print("FIM")
