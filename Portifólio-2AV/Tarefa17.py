class Grafo:
    def __init__(self):
        self.lista_adjacencia = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_adjacencia:
            self.lista_adjacencia[vertice] = []

    def adicionar_arco(self, origem, destino):
        self.adicionar_vertice(origem)
        self.adicionar_vertice(destino)
        self.lista_adjacencia[origem].append(destino)

    def exibir_lista_adjacencia(self):
        for vertice, vizinhos in sorted(self.lista_adjacencia.items()):
            print(f"{vertice}: {' | '.join(map(str, vizinhos))}")


# Criar o grafo
grafo = Grafo()

# Adicionar vértices e arcos
print("\nLista de adjacência do grafo: ")
grafo.adicionar_arco(0, 0)
grafo.adicionar_arco(0, 2)
grafo.adicionar_arco(2, 6)
grafo.adicionar_arco(6, 0)
grafo.adicionar_arco(6, 2)
grafo.adicionar_arco(6, 4)
grafo.adicionar_arco(1, 3)
grafo.adicionar_arco(1, 3)
grafo.adicionar_arco(3, 7)
grafo.adicionar_arco(8, 5)

# Exibir lista de adjacência
grafo.exibir_lista_adjacencia()
print("")
