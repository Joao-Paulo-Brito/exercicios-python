"""
Exercício 010:
    Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

    . O total a pagar com desconto de 10%
    . O valor de cada parcela num parcelamento de 3x sem juros
    . A comissão do vendedor, no caso da venda ser a vista(5% sobre o valor com desconto)
    . A comissão do vendedor, no caso da cenda ser parcelada(5% sobre o valor total)
"""
# Entrada de dados
print("------------------Mercadinho do seu João-------------------")
print("          NÃO PERCA AS PROMOÇÕES DO DIA DOS PAIS           ")
print("|-------------------------------|")
print("|    Geladeira por R$900,00     |")
print("|    Cafeteira por R$300,00     |")
print("|Fogão quatro bocas por R$950,00|")
print("|-------------------------------|")
print("-----------------------------------------------------------")
print("Digite o valor da sua compra")
valor = int(input())

# Cálculo
desconto = float(valor-(valor*10/100))
parcela = float(valor/3)
comissao_vista = float(desconto-(desconto*5/100))
comissao_parcelada = float(valor-(valor*5/100))

# Saída de dados
print("--------------------------------------------------")
print(f"Total a pagar com desconto de 10%: R${desconto:.2f}")
print(f"Valor das parcelas de 3x sem juros: R${parcela:.2f}")
print(f"A comissão do vendedor com venda a vista: R${comissao_vista:.2f}")
print(f"A comissão do vendedor com venda parcelada: R${comissao_parcelada:.2f}")
print("--------------------------------------------------")
