"""
Exercício 029:
    Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
# Entrada de dados
print("\nQual é o nome do aluno ?")
aluno = str(input())

print(f"\nDigite 4 notas de {aluno} para cálcular a média delas:")
notas = []

# Formando lista
for cont in range(1, 5):
    n = float(input())
    notas.append(n)

# Cálculo da média
media = float(sum(notas)/len(notas))

# Saída de dados
print(f"\nNotas do aluno {aluno}: ")
print(notas)

print("\nMédia das notas: ")
print(media)

# Avaliação
if media >= 7:
    print(f"\nO aluno {aluno} está APROVADO!")
else:
    print(f"\nO aluno {aluno} está REPROVADO!")
