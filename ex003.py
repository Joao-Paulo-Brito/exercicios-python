"""
Exercício 003:
    Leia uma temperatura em graus Celcius e converta para graus Fahrenheit, a formula é:
    F = C*(9/5) + 32
    # OBS: F = Fahrenheit, C = Celcius
"""

# Entrada de dados
print("Digite uma temperatura em Celcius: ")
Celcius = float(input())

# Conversão
Fahrenheit = float(Celcius*(9/5)+32)

# Saída de dados
print("\n CONVERTENDO... \n")
print(f"O valor de {Celcius}°C em Fahrenheit é igual a: {Fahrenheit}°F")
