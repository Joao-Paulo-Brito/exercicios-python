"""
    Exercício 046:
    Faça uma calculadora que peça ao usuário o tipo de operação que ele quer fazer e os números para realizar a operação
podendo ser adição, subtração, divisão, multiplicação, potenciação ou raiz quadrada
"""


def calculadora():
    # Casos escolhidos
    match operacao:
        case '+':
            print("\nDigite os números que você quer somar:")
            n1 = int(input("Primeiro número: "))
            n2 = int(input("Segundo número: "))
            return n1 + n2
        case '-':
            print("\nDigite os números que você quer subtrair:")
            n1 = int(input("Primeiro número: "))
            n2 = int(input("Segundo número: "))
            return n1 - n2
        case 'x':
            print("\nDigite os números que você quer multiplicar:")
            n1 = int(input("Primeiro número: "))
            n2 = int(input("Segundo número: "))
            return n1 * n2
        case '/':
            print("\nDigite os números que você quer dividir:")
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
            return n1 / n2


# Variáveis
operacao = str()

# Entrada de dados
print("-"*30+"Calculadora"+"-"*30)
while operacao not in ['+', '-', 'x', '/']:
    print("Digite o tipo de operação que você quer realizar: ")
    print("Digite '+' para adição")
    print("Digite '-' para subtração")
    print("Digite 'x' para multiplicação")
    print("Digite '/' para divisão")
    operacao = str(input())

# Validação
    if operacao not in ['+', '-', 'x', '/']:
        print("\nOperação inválida, tente novamente!\n")

resultado = calculadora()

print(f"\nResultado da operação: {resultado}")
