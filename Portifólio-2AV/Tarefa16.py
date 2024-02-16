def menor_caminho_guloso(grafo, inicio, destino):
    caminho = [inicio]
    custo_total = 0

    while caminho[-1] != destino:
        proximo_no = seleciona_proximo_no(grafo, caminho)
        caminho.append(proximo_no)
        custo_total += grafo[caminho[-2]][proximo_no]

    return caminho, custo_total


def seleciona_proximo_no(grafo, caminho):
    no_atual = caminho[-1]
    candidatos = set(grafo[no_atual].keys()) - set(caminho)

    # Seleciona o candidato com a menor distância
    proximo_no = min(candidatos, key=lambda x: grafo[no_atual][x])
    return proximo_no


# Distâncias dos pontos do grafo
grafo = {
    'a': {'b': 16, 'f': 21, 'e': 9},
    'b': {'a': 16, 'c': 5, 'f': 11, 'd': 6},
    'c': {'b': 5, 'd': 10},
    'd': {'b': 6, 'c': 10, 'f': 14, 'e': 18},
    'e': {'a': 9, 'f': 33, 'd': 18},
    'f': {'a': 21, 'b': 11, 'd': 14, 'e': 33}
}

inicio = 'a'
destino = 'c'

caminho, custo_total = menor_caminho_guloso(grafo, inicio, destino)

print(f'\nMenor caminho de {inicio} até {destino}: {caminho}')
print(f'Custo total do caminho: {custo_total}')
