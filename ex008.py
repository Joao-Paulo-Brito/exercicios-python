"""
Exercício 008:
    Faça um programa que leia o número, e caso ele seja positivo, calcule e mostre:
    .O quadrado desse número
    .A raiz desse número
caso o número for negativo, informe uma mensagem de erro.
"""
# Importação da biblioteca "math"
import math

# Entrada de dados
print("Digite um número inteiro")
numero = int(input())

if numero > 0:
    quadrado = int(numero*numero)
    raiz = math.sqrt(numero)
else:
    print("Erro, número negativo, tente novamente!")

print(f"O quadrado de {numero} é igual a {quadrado}")
print(f"e a raiz de {numero} é igual a {raiz}")
