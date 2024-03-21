"""
    Exercício 047:
    Faça um simulador de caixa eletrônico onde o usuário possa verificar o saldo no banco, realizar saque, depositar
dinheiro e sair do programa. Faça uma função para cada uma das operações anteriores, utilizando parâmetros se
necessário.

Requsitos:

    Verificar saldo:

        - Ao escolher essa opção, o programa deve exibir o saldo atual da conta.

    Depositar dinheiro:

        - O usuário deve ser capaz de inserir uma quantia para depositar na conta.
        - A quantia deve ser positiva.
        - Após um depósito bem-sucedido, o saldo da conta deve ser atualizado e uma mensagem de confirmação deve ser
        exibida.

    Sacar Dinheiro:

        - O usuário deve ser capaz de inseriri uma quantia para sacar da conta.
        - A quantia deve ser positiva e não deve exceder o saldo atual.
        - Após um saque bem-sucedido, o saldo da conta deve ser atualizado e uma mensagem de confirmação deve ser
        exibida.

    Sair:

        O usuário deve ser capaz de sair do programa escolhendo essa opção

    Validação de entrada:

        - O programa deve lidar com entradas inválidas de forma adequada, exibindo mensagens de erro quando aplicável.

    Interface do Usuário:

        - O programa deve exibir um menu de opções para o usuário permitir a seleção de ações a serem realizadas.
        - As opções do menu devem ser apresentadas em um loop, permitindo múltiplas operações até que o usuário escolha
        sair.

    O saldo inicial começa com R$1000,00

"""


def verificar_saldo():
    return f"\nSeu saldo atual: R${saldo}\n"


def depositar_dinheiro(saldo, deposito):
    saldo += deposito
    return saldo


def sacar_dinheiro(saldo, saque):
    saldo -= saque
    return saldo


# Variáveis
saldo = float(1000)
resposta = int()

while resposta != 4:

    # Entrada de dados
    print("-" * 30 + "Banco JP" + "-" * 30)
    print("Digite os seguintes números para realizar uma ação no banco:")
    print("1 - Verificar saldo na conta")
    print("2 - Depositar dinheiro")
    print("3 - Sacar dinheiro")
    print("4 - Sair")
    print("-" * 68)
    resposta = int(input())

    match resposta:
        case 1:
            print(verificar_saldo())
        case 2:
            print("Qual é a quantia que você quer depositar ?")
            quantia = float(input())

            saldo = depositar_dinheiro(saldo, quantia)
            print(f"\nDeposito de R${quantia}0. Operação bem sucedida!\n")
        case 3:
            print("Qual é a quantia de que você quer sacar ?")
            quantia = float(input())

            saldo = sacar_dinheiro(saldo, quantia)
            print(f"Saque de R${quantia}0 realizado. Operação bem sucedida!")
        case 4:
            print("\nSAINDO...\n")
