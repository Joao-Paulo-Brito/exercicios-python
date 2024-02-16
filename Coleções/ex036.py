"""
Exercício 036:
    Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos e depois mostre a soma
deles, depois pergunte se o usuário deseja adicionar ou remover valores, caso queira continuar o programa, digitar o
número 1, caso não, encerre o programa com o número 2.
"""
# Variáveis
vet = []
resposta = int(0)
resposta2 = str()

# Entrada de dados
print("Digite 6 números inteiros")
for cont in range(1, 7):
    vet.append(input(f"Digite o {cont}° valor: "))

# Saída de dados
print("\nValores do vetor:")
for cont in range(len(vet)):
    print(vet[cont])

while resposta != 2:
    print("\nDeseja continuar com o programa ?")
    print("Digite 1 para sim")
    print("Digite 2 para não")
    resposta = int(input())

    if resposta == 1:

        while resposta2 != 'adicionar' or resposta2 != 'remover':
            print("\nVocê quer adicionar ou remover um valor ?")
            resposta2 = str(input()).lower()

            if resposta2 == 'adicionar':
                vet.append(input("Digite o valor a ser adicionado: "))
                break
            elif resposta2 == 'remover':
                vet.remove(input("Digite o valor a ser removido: "))
                break
            else:
                print("Resposta errada! digite se quer adicionar ou remover um valor, tente novamente")

    elif resposta == 2:
        print("\nPrograma encerrado\n")
    else:
        print("\nResposta errada! digite apenas 1 ou 2, tente novamente")

print(f"Valores do vetor: {vet}")
