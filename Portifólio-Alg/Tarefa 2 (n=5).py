import itertools
import time


# Função para gerar e imprimir permutações das cidades
def permutacao(cidades):
    # Gera todas as permutações possíveis das cidades, excluindo a cidade 'A' inicial
    permutacoes = itertools.permutations(cidades[1:])
    for p in permutacoes:
        # Adiciona 'A' no início e no final de cada permutação
        permutacao_com_a = ('A',) + p + ('A',)
        # Imprime a permutação como uma sequência de cidades
        print(' '.join(permutacao_com_a))


if __name__ == "__main__":
    # Define a lista de cidades
    cidades = ('A', 'B', 'C', 'D', 'E')

    # Entrada de dados
    print("Permutações possíveis para 5 cidades com a cidade 'A' sendo a posição inicial:")

    # Tempo de início
    inicio = time.perf_counter()

    permutacao(cidades)

    # Registra o tempo no final da execução
    fim = time.perf_counter()

    # Calcula o tempo decorrido durante a execução
    tempo_decorrido = fim - inicio

    # Saída de dados
    print(f"Tempo de execução: {tempo_decorrido:.6f} segundos")
