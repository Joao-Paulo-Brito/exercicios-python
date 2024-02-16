"""
Exercício 030:
    Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
# Variáveis
vet = []
vogais = ['a', 'e', 'i', 'o', 'u']
caractere = str('abc')
consoantes = int(0)

# Entrada de dados
print("Digite 10 caracteres")
while len(caractere) > 1 or caractere.isnumeric():
    # Reinicia contagem de consoantes
    consoantes = 0

    for contador in range(1, 11):
        caractere = str(input(f"Digite o {contador}° caractere: ")).lower()

        # Verificação
        if len(caractere) > 1:
            print("\nError! digite um caractere de cada vez, tente novamente\n")
            break
        elif caractere.isnumeric():
            print("\nError! digite apenas letras, não números, tente novamente\n")
            break
        else:
            vet.append(caractere)
            if caractere not in vogais:
                consoantes += 1

print(f"\nQuantidade de consoantes digitadas: {consoantes}")
