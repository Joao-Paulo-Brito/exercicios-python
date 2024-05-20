"""
1) (Enem 2016) Em uma cidade, o número de casos de dengue confirmados aumentou consideravelmente nos últimos dias. A prefeitura resolveu desenvolver uma ação contratando funcionários para ajudar no combate à doença, os quais orientarão os moradores a eliminarem criadouros do mosquito Aedes aegypti, transmissor da dengue. A tabela apresenta o número atual de casos confirmados, por região da cidade.

Tabela apresenta o número atual de casos confirmados de dengue por região.

dados = [237, 262, 158, 159, 160, 278, 300, 278]

A prefeitura optou pela seguinte distribuição dos funcionários a serem contratados:

I. 10 funcionários para cada região da cidade cujo número de casos seja maior que a média dos casos confirmados. 

II. 7 funcionários para cada região da cidade cujo número de casos seja menor ou igual à média dos casos confirmados.

Quantos funcionários a prefeitura deverá contratar para efetivar a ação?

A) 59

B) 65

C) 68

D) 71

E) 80

R=
(237 + 262 + 158 + 159 + 160 + 278 + 300 + 278)/8 = 229

quantidade de dados maior que a média = 5

quantidade de dados menor ou igual que a média = 3

5 x 10 funcionários = 50

3 x 7 funcionários = 21

total de funcionários = 50 + 21 = 71

-->Python:

dados = [237, 262, 158, 159, 160, 278, 300, 278]
funcionarios = int(0)

media = sum(dados)/len(dados)

print(f"Média: {media}\n")

for dado in dados:
    if dado > media:
        funcionarios += 10
        print(dado, " > media")
    elif dado <= media:
        funcionarios += 7
        print(dado, " <= media")

print(f"\nQuantidade de funcionários contratados: {funcionarios}")



2) (Enem) A tabela a seguir mostra a evolução da receita bruta anual nos três últimos anos de cinco microempresas (ME) que se encontram à venda.

Tabela com evolução da receita bruta anual nos três últimos anos de cinco microempresas (ME) que se encontram à venda

AlfinetesV = [200, 220, 240]

Balas W = [200, 230, 200]

Chocolates X = [250, 210, 215]

Pizzaria Y = [230, 230, 230]

Tecelagem Z = [160, 210, 245]

Um investidor deseja comprar duas das empresas listadas na tabela. Para tal, ele calcula a média da receita bruta anual dos últimos três anos (de 2009 até 2011) e escolhe as duas empresas de maior média anual.

As empresas que este investidor escolhe comprar são

A) Balas W e Pizzaria Y.

B) Chocolates X e Tecelagem Z.

C) Pizzaria Y e Alfinetes V.

D) Pizzaria Y e Chocolates X.

E) Tecelagem Z e Alfinetes V.

R=

Media_Alfinetes = (200 + 220 + 240)/3 = 220

Media_Balas = (200 + 230 + 200)/3 = 630/3 = 210

Media_Chocolates = (250, 210, 215)/3 = 675/3 = 225

Media_Pizzaria = (230, 230, 230)/3 = 690/3 = 230

Media_Tecelagem = (160, 210, 245)/3 = 615/3 = 205

Maiores médias = 230 e 225

Pizzaria Y e Chocolates X

letra D

. Python:
# Dados
AlfinetesV = [200, 220, 240]
BalasW = [200, 230, 200]
ChocolatesX = [250, 210, 215]
PizzariaY = [230, 230, 230]
TecelagemZ = [160, 210, 245]

dados_totais = [AlfinetesV, BalasW, ChocolatesX, PizzariaY, TecelagemZ]

medias = []
media = int(0)

# Cálculo das médias
for listas in dados_totais:
    for dado in listas:
        media += dado
    media = media/len(listas)
    medias.append(round(media, 2))
    media = 0

empresas = ['AlfinetesV', 'BalasW', 'ChocolatesX', 'PizzariaY', 'TecelagemZ']

empresas_medias = {chave: valor for chave, valor in zip(empresas, medias)}

# Ordenando as médias em ordem crescente
medias.sort()

# Duas maiores médias
maiores_medias = [max(medias), medias[len(medias) - 2]]

empresas = {}

for chave, valor in empresas_medias.items():
    if valor in maiores_medias:
        empresas[chave] = valor

print(f"\nMédias: {medias}")
print(f"Maiores médias: {maiores_medias}")
print(f"Empresas escolhidas: {empresas}\n")

3) (Enem) Uma equipe de especialistas do centro meteorológico de uma cidade mediu a temperatura do ambiente, sempre no mesmo horário, durante 15 dias intercalados, a partir do primeiro dia de um mês. Esse tipo de procedimento é frequente, uma vez que os dados coletados servem de referência para estudos e verificação de tendências climáticas ao longo dos meses e anos.
As medições ocorridas nesse período estão indicadas no quadro:

Em relação à temperatura, os valores da média, mediana e moda são, respectivamente, iguais a

A) 17 °C, 17 °C e 13,5 °C.

B) 17 °C, 18 °C e 13,5 °C.

C) 17 °C, 13,5 °C e 18 °C.

D) 17 °C, 18 °C e 21,5 °C.

E) 17 °C, 13,5 °C e 21,5 °C.

R=
# Contador dos valores dos dados e ordenação do dicionário
from collections import Counter, OrderedDict

dados = [15.5, 14, 13.5, 18, 19.5, 20, 13.5, 13.5, 18, 20, 18.5, 13.5, 21.5, 20, 16]
dados.sort()
print(f"Dados: {dados}")

# Média
media = sum(dados)/len(dados)
print(f"\nMédia: {media}")

# Mediana
mediana = float(0)
for cont in range(len(dados)):
    if cont == len(dados)//2:
        mediana = dados[cont]

print(f"\nMediana: {mediana}")

# Moda
moda = OrderedDict(Counter(dados))
print("\nQuantidade de vezes que cada valor aparece na lista:")
print(moda)

for chave, valor in moda.items():
    if valor == max(moda.values()):
        print(f"\nModa: {chave}")

"""
