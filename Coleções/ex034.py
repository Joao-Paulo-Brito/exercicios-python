"""
Exercício 034:
    Faça uma lista de produtos: Lápis->R$1,75, Caneta->R$1,90, borracha->R$2,00, caderno->R$15,00. O usuário ira digitar
quais produtos ele quer e depois calcular o total que ele irá pagar. Faça tudo o que for necessário para o funcionamento
dessa compra, use tuplas para isso.
"""
# Variáveis
continua = int(0)
total = float(0)
quantidade = int(-1)
resposta = str()

# Tuplas
produtos = 'lapis', 1.75, 'caneta', 1.90, 'borracha', 2.00, 'caderno', 15.00
pedidos = ()

# Entrada de dados

print('-'*45)
print('Listagem de preços')
print('-'*45)
for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>10}')
print('-'*45)

while continua != 2:
    while resposta not in ['lapis', 'borracha', 'caneta', 'caderno']:
        print("\nDigite o produto que você quer: ")
        resposta = str(input().lower())
        if resposta not in ['lapis', 'borracha', 'caneta', 'caderno']:
            print("Resposta inválida, tente novamente!")

    while quantidade < 0:
        print(f"\nQual é a quantidade de {resposta} ?")
        quantidade = int(input())

    # Validação
    if resposta == 'lapis':
        total += quantidade * 1.75
        pedidos = 'lapis', quantidade
    elif resposta == 'caneta':
        total += quantidade * 1.90
        pedidos = 'caneta', quantidade
    elif resposta == 'borracha':
        total += quantidade * 2
        pedidos = 'borracha', quantidade
    elif resposta == 'caderno':
        total += quantidade * 15
        pedidos = 'caderno', quantidade
    else:
        print("Resposta inválida, tente novamente!")

    print("\nVocê ainda quer continuar ?")
    print("Digite 1 para sim")
    print("Digite 2 para não")
    continua = int(input())

# Total
print("Você pediu:")
print('-'*45)
for item in range(len(pedidos)):
    if item % 2 == 0:
        print(f'{pedidos[item]:.<30}', end='')
    else:
        print(f'{pedidos[item]:>10}x')
print('-'*45)
print(f"\nO total da sua compra é: R${total}")
