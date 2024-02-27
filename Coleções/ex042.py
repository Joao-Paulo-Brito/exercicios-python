"""
Exercício 042:
    Elabore um programa que calcule um valor a ser pago pelo produto, considerando seu preço normal e condição de
pagamento:
A vista dinheiro/cheque: 10% de desconto.
A vista no cartão: 5% de desconto.
Em até 2x no cartão: preço normal.
3x ou mais no cartão: 20% de juros.
"""


def plural():
    if compra == 'Tv' and quantidade > 1:
        return 'TVs'
    elif compra == 'Celular' and quantidade > 1:
        return 'Celulares'
    elif compra == 'Geladeira' and quantidade > 1:
        return 'Geladeiras'
    elif compra == 'Playstation 4' and quantidade > 1:
        return 'Playstations 4'
    elif compra == 'Fogão' and quantidade > 1:
        return 'Fogões'
    else:
        return compra


# Variáveis
produtos = 'Tv', 1200, 'Celular', 900, 'Geladeira', 1500, 'Playstation 4', 1100, 'Fogão', 500
compra = str('')
quantidade = int(0)
pagamento = int(0)
preco = int(0)
total = float(0)

# Propaganda
print("-"*40)
print(" "*14+"Atacadão JP")
print("-"*40)

for item in range(len(produtos)):
    if item % 2 == 0:
        # Preenchimento do espaço com no máximo 30 caracteres, tendo o "." como caractere extra para preencher o espaço
        # restante
        print(f"{produtos[item]:.<30}", end='R$')
    else:
        print(f"{produtos[item]}")

print("-"*40)

# Entrada de dados
# Escolha do produto
while (compra not in produtos) or (produtos.index(compra) % 2 != 0):
    print("\nDigite o produto que deseja comprar: ")
    compra = str(input()).capitalize()  # Primeira letra maiúscula e o resto minuscula

    # Condição
    if compra not in produtos:
        print("Erro, o produto digitado não está no estoque, tente novamente!")
    elif produtos.index(compra) % 2 != 0:
        print("Erro, o produto digitado não está no estoque, tente novamente!")
    else:
        # Quantidade
        print(f"\nDigite a quantidade de {compra} que você quer: (mínimo 1)")
        quantidade = int(input())

        # Condição 2
        if quantidade <= 0:
            print("Erro, a quantidade mínima do produto deve ser 1")
        else:
            print(f"\nProduto escolhido: {compra}")
            print(f"Quantidade: {quantidade}")
            print("Adicionado ao carrinho")

print("\nDigite um número para os métodos de pagamento abaixo:")
print("-" * 80)
print("Digite 1 para compra a vista dinheiro/cheque: 10% de desconto.\n"
      "Digite 2 para compra a vista no cartão: 5% de desconto.\n"
      "Digite 3 para compra em 2x no cartão: preço normal.\n"
      "Digite 4 para compra em 3x ou mais no cartão: 20% de juros.")
print("-" * 80)
while pagamento not in [1, 2, 3, 4]:
    pagamento = int(input())

    # Condição 3
    if pagamento not in [1, 2, 3, 4]:
        print("Número inválido, tente novamente!")
    else:
        print(f"\nOpção {pagamento} selecionada")

# Saída de dados
preco = produtos.index(compra)+1
match pagamento:
    case 1:
        total = (produtos[preco] - (produtos[preco] * 10/100)) * quantidade
        if quantidade == 1:
            print(f"\nVocê deverá pagar R${total},00 para a compra de {compra}")
        else:
            compra = plural()
            print(f"\nVocê deverá pagar R${total},00 para a compra de {quantidade} {compra}")
    case 2:
        total = (produtos[preco] - (produtos[preco] * 5/100)) * quantidade
        if quantidade == 1:
            print(f"\nVocê deverá pagar R${total},00 para a compra de {compra}")
        else:
            compra = plural()
            print(f"\nVocê deverá pagar R${total},00 para a compra de {quantidade} {compra}")
    case 3:
        total = (produtos[preco]/2) * quantidade
        if quantidade == 1:
            print(f"\nVocê deverá pagar R${total},00 para a compra de {compra}, em cada mês, em 2x")
        else:
            compra = plural()
            print(f"\nVocê deverá pagar R${total},00 para a compra de {quantidade} {compra}, em cada mês, em 2x")
    case 4:
        # 3x ou mais
        parcelas = int(0)
        while parcelas < 3:
            print("\nDigite quantas parcelas você quer no cartão ? (3x ou mais)")
            parcelas = int(input())

            if parcelas < 3:
                print("\nErro, o número de parcelas para a opção 4 deve ser igual ou maior que 3")
            else:
                total = ((produtos[preco] + (produtos[preco] * 20 / 100)) / parcelas) * quantidade
                if quantidade == 1:
                    print(f"\nVocê deverá pagar R${total},00 para a compra de {compra}, em cada mês, em {parcelas}x")
                else:
                    compra = plural()
                    print(f"\nVocê deverá pagar R${total},00 para a compra de {quantidade} {compra}, em cada mês, em "
                          f"{parcelas}x")
