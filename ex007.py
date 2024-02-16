"""
Exercício 007:
    A importancia de R$780.000,00 será dividida entre três ganhadores de um concurso,
Sendo que da quantia total:
.O primeio ganhador receberá 46%;
.O segundo receberá 32%;
.O terceiro receberá o restante;
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""
total = int(780000)

primeiro = 46/100*total

segundo = 32/100*total

terceiro = 22/100*total
print("|-----------------------------PRÊMIO----------------------------|")
print(f"|O prêmio é de {total}                                           |")
print(f"|O primeiro vencedor receberá 46%, ou seja, R${primeiro}          |")
print(f"|O segundo receberá 32%, ou seja, R${segundo}                    |")
print(f"|E o terceiro receberá os 22% restantes, ou seja, R${terceiro}    |")
print("|---------------------------------------------------------------|")
