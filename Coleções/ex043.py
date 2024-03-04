"""
Exercício 043:
    Faça um programa que leia o nome de 4 alunos, as notas da primeira avaliação e segunda avaliação deles, mostre a
média e caso a nota final seja maior que meio ponto a mais da nota inteira, ou seja, caso o aluno tirar uma nota maior
que 9.5 por exemplo, pode arredondar para 10, caso for menor, arredonde para 9. Depois disso imprima de forma aleatória
os nomes e as notas de cada aluno.
"""
# Biblioteca random e math
import random
import math

# Variáveis
alunos = []
notas = []
medias = []
resultado = {}

# Entrada de dados
for cont in range(4):
    # Nomes
    alunos.append(str(input(F"\nDigite o nome do {cont+1}° aluno: ")))

    # Notas
    notas.append(float(input(f"Digite a nota da 1° avaliação de {alunos[cont]}: ")))
    notas.append(float(input(f"Digite a nota da 2° avaliação de {alunos[cont]}: ")))

# Cálculo da média
cont2 = int(1)
for cont in range(4):
    media = float((notas[cont+cont2-1] + notas[cont+cont2])/2)
    cont2 += 1

    # Arredondamento
    if media - int(media) > 0.5:
        media = math.ceil(media)
    else:
        media = math.floor(media)

    medias.append(media)

# Atribuindo alunos as suas médias
for cont in range(4):
    chave = alunos[cont]
    valor = medias[cont]

    # Resultado final
    resultado[chave] = valor

# Embaralhando a ordem dos alunos
ordem = list(resultado.keys())
random.shuffle(ordem)

# Saída de dados
print('\nResultado:')
for chave, valor in resultado.items():
    print(f"Aluno: {chave}, nota final: {valor}")

print("\nEmbaralhando a ordem:")
for chave in ordem:
    print(f"Aluno: {chave}, nota final: {resultado.get(chave)}")
