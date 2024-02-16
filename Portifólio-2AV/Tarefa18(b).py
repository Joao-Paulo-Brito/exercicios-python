from collections import deque

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.lista_adj = {v: [] for v in range(vertices)}

    def adicionar_aresta(self, v, w):
        self.lista_adj[v].append(w)


def bfs(grafo, inicio):
    visitados = set()
    fila = deque([inicio])
    passos = []

    while fila:
        vertice = fila.popleft()
        if vertice not in visitados:
            passos.append(vertice)
            visitados.add(vertice)
            fila.extend(vizinho for vizinho in grafo.lista_adj[vertice] if vizinho not in visitados)

    return passos


def dfs(grafo, inicio):
    visitados = set()
    passos = []

    def dfs_recursiva(v):
        passos.append(v)
        visitados.add(v)
        for vizinho in grafo.lista_adj[v]:
            if vizinho not in visitados:
                dfs_recursiva(vizinho)

    dfs_recursiva(inicio)
    return passos


# Grafo fornecido
grafo = Grafo(12)
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(0, 4)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(1, 5)
grafo.adicionar_aresta(2, 3)
grafo.adicionar_aresta(3, 7)
grafo.adicionar_aresta(4, 8)
grafo.adicionar_aresta(5, 4)
grafo.adicionar_aresta(6, 5)
grafo.adicionar_aresta(6, 10)
grafo.adicionar_aresta(6, 2)
grafo.adicionar_aresta(7, 11)
grafo.adicionar_aresta(7, 6)
grafo.adicionar_aresta(8, 9)
grafo.adicionar_aresta(9, 5)
grafo.adicionar_aresta(9, 8)
grafo.adicionar_aresta(10, 9)
grafo.adicionar_aresta(11, 10)

# Busca em Largura (BFS)
print("BFS:")
bfs_passos = bfs(grafo, 0)
print("Rastreamento (BFS):", bfs_passos)
print()

# Busca em Profundidade (DFS)
print("DFS:")
dfs_passos = dfs(grafo, 0)
print("Rastreamento (DFS):", dfs_passos)
