"""
Exercício 012
    Calcule a média ponderada das notas de 3 provas, a primeira e a segunda prova tem peso 1 e a terceira tem peso 2. Ao
final, mostrar a média do aluno, e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 10 pontos
"""
# Entrada de dados
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))
nota3 = float(input("Digite a nota da terceira avaliação: "))

# Cálculo
media_pon = round((nota1+nota2+nota3*2)/4, 2)

# Condição
if media_pon < 6:
    print(f"\nO aluno tirou {media_pon}, ele está reprovado")
else:
    print(f"\nO aluno tirou {media_pon}, logo ele está aprovado!")
