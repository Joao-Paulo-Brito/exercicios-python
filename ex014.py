"""
Exercício 014:
    - Crie uma função “verificar_senha” no qual retorna true caso a senha inserida for correta e false caso o contrário
Logo após elabore um “mini-sistema” de checar a senha inserida, onde o usuário tem 3 tentativas de senha e caso esse
número seja ultrapassado o programa é encerrado.
"""
# Varável cont
cont = int()

# Entrada de dados
while cont < 3:
    print("\nVerificar senha")
    print("Digite a sua senha: ")
    senha = str(input())

    # Vericicando senha
    if senha != '123':
        print("\n Senha incorreta!")
        cont += 1
        if cont >= 3:
            print("\nNúmero de tentativas ultrapassada")
    else:
        print("\nSenha correta!")
        break
