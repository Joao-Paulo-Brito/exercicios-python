from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {v: [] for v in range(vertices)}

    def add_edge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)


def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            queue.extend(adjacent for adjacent in graph.adj_list[vertex] if adjacent not in visited)


def dfs(graph, start):
    visited = set()

    def dfs_recursive(v):
        print(v, end=' ')
        visited.add(v)
        for neighbor in graph.adj_list[v]:
            if neighbor not in visited:
                dfs_recursive(neighbor)

    for vertex in range(graph.vertices):
        if vertex not in visited:
            dfs_recursive(vertex)


# Grafo: 0-1 1-2 1-3 3-4 3-5 1-6 0-7 7-8 7-9 8-6
graph = Graph(10)
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 5)
graph.add_edge(1, 6)
graph.add_edge(0, 7)
graph.add_edge(7, 8)
graph.add_edge(7, 9)
graph.add_edge(8, 6)

# Busca em Largura (BFS)
print("BFS:")
bfs(graph, 0)
print()

# Busca em Profundidade (DFS)
print("DFS:")
dfs(graph, 0)
