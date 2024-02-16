"""
Exercício 013:
    Usando o switch(match) case, escreva um número que leia um número inteiro de 1 a 7, cada um desses números representa um
dia da semana, domingo é número 1, segunda é número 2 e assim por diante
"""
# Entrada de dados
print("\nDigite um número inteiro de 1 a 7 para saber o dia da semana:")
numero = int(input())

# Switch
match numero:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
