import itertools
import timeit
import time

# Variável para contar o número de permutações
cont = 0

# Tempo inicial da execução
inicio = time.time()


# Função para gerar e imprimir permutações das cidades
def permutacao(cidades):
    # Gera todas as permutações possíveis das cidades, excluindo a cidade 'A' inicial
    permutacoes = itertools.permutations(cidades[1:])
    for p in permutacoes:
        global cont
        cont += 1
        # Limitação para o tempo de execução não ser longo, dividindo o resultado por 100.000
        if cont == int(87178291200 / 100000):
            # Tempo de término da execução
            fim = time.time()
            # Calcula e imprime o tempo decorrido
            print(fim - inicio)
            return 1
        # Adiciona 'A' no início e no final de cada permutação
        permutacao_com_a = ('A',) + p + ('A',)
        # Imprime a permutação como uma sequência de cidades
        print(' '.join(permutacao_com_a))


if __name__ == "__main__":
    # Define a lista de cidades
    cidades = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O')

    # Exibe a mensagem inicial
    print("Permutações possíveis para 15 cidades com a cidade 'A' sendo a posição inicial:")

    # Usa o timeit para medir o tempo de execução com precisão
    tempo_decorrido = timeit.timeit(lambda: permutacao(cidades), number=1)

    # Saída de dados
    print(f"Tempo de execução: {tempo_decorrido:.6f} segundos")
