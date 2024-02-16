"""
Exercício 033:
    Faça uma tupla com os times do brasileirão: Coríntias, Palmeiras, Santos, Grêmio, Cruzeiro, Coritiba, Avaí, Atlético
mineiro. Mostre quais são os 5 primeiros times, os 4 últimos e em qual posição o Coritiba está
"""
times = ('Coríntias', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Coritiba', 'Avaí', 'Atléticomineiro')

# 5 primeiros times
print("\n5 primeiros times:")
print(times[:5])

# 4 últimos times
print("\n4 últimos elementos: ")
print(times[-4:])

# Posição de Curitíba
print(f"\nCoritiba está na {times.index('Coritiba')+1}° posição")  # Adiciona 1 para uma contagem normal
