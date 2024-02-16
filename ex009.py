"""
Exercício 009:
    Digite as notas da primeira e segunda avaliação do semestre do aluno e calcule a média, se a média for maior que 8,
o aluno está aprovado, se for menor que 8, o aluno precisa fazer recuperação, se for menor que 4, o aluno está
reprovado.
"""
# Entrada de dados
print("Digite a nota da primeira avaliação do aluno: ")
nota1 = int(input())

print("Digite a nota da segunda avaliação do aluno: ")
nota2 = int(input())

# Verificação
if nota1 < 0 or nota2 < 0:
    print("Nota inválida, tente novamente")
elif nota1 > 10 or nota2 > 10:
    print("Nota inválida, tente novamente")

# Cálculo da média
media = round(float((nota1+nota2)/2), 2)

# Saída de dados
print(f"A média desse aluno é: {media}\n")

# Avaliação
if media >= 8:
    print("Aluno aprovado")
elif 4 < media < 8:
    print("Aluno em recuperação")
else:
    print("Aluno reprovado")
