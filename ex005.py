"""
Exercício 005:
    Leia uma velocidade em Km/h e converta em m/s
"""

# Entrada de dados
print("Digite uma velocidade em km/h")
km = float(input())

# Calculo
m = round(float(km/3.6), 2)  # Funcão round() limita a quantidade de casas decimais em números reais(float)

# Saída de dados
print(f"A velocidade de {km}km/h é igual a {m}m/s")
