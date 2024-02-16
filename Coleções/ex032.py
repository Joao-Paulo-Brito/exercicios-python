"""
Exercício 032:
    Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0.
"""
# Entrada de dados
notas_alunos = []

# Notas dos 10 alunos
for cont in range(1, 4):
    # Lista das 4 notas do alunos
    notas = [float(input(f"Digite a {j}° nota do {cont}° aluno: "))for j in range(1, 5)]
    print("")

    # Cálculo da média
    media = float(sum(notas)/len(notas))

    # Adicionando a nota final ao vetor das notas dos alunos
    notas_alunos.append(media)

# Contando o número de alunos aprovados
alunos_aprovados = sum(media >= 7 for media in notas_alunos)

# Saída de dados
print(f"Número de alunos aprovados: {alunos_aprovados}")
