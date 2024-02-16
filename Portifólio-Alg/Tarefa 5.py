import time


# Como gerar números primos em um intervalo numérico
# Função para verificar os números primos
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    # Usuário escolhe o intervalo
    print("Digite um valor: ")
    n = int(input())
    # Iniciação da contagem de tempo
    inicio = time.time()
    print(f'Os números primos menores que {n} são: ')

    for i in range(n + 1):
        if primo(i):
            print(i, end=' ')

# Fim da contagem de tempo
fim = time.time()

execution = round(float(fim-inicio), 3)

print(f"\nTempo de execução em segundos: {execution}")
