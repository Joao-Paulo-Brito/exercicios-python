"""
Exercício 004:
    Leia uma temperatura em graus Fahrenheit e converta para graus Celcius, a formula é:
    C = 5*(F-32)/9
"""

#Entrada de dados
print("Digite uma temperatura em Fahrenheit")
fahrenheit = float(input())

# Conversão
celcius = 5*(fahrenheit-32)/9

# Saída de dados
print(f"A temperatura {fahrenheit}°F em graus celcius é: {celcius}°C")
