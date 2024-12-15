class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def bellman_ford(V, E, edges, source):
    distance = [float('inf')] * V
    distance[source] = 0

    for _ in range(V - 1):
        for edge in edges:
            u, v, weight = edge.u, edge.v, edge.weight
            if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight

    for edge in edges:
        u, v, weight = edge.u, edge.v, edge.weight
        if distance[u] != float('inf') and distance[u] + weight < distance[v]:
            print("Граф содержит отрицательный цикл!")
            return False

    print(f"Кратчайшие расстояния от вершины {source} до остальных вершин:")
    for i in range(V):
        if distance[i] == float('inf'):
            print(f"Вершина {i}: Недостижима")
        else:
            print(f"Вершина {i}: {distance[i]}")
    return True


if __name__ == "__main__":
    V = int(input("Введите количество вершин: "))
    E = int(input("Введите количество рёбер: "))

    edges = []
    print("Введите рёбра в формате (u v вес):")
    for _ in range(E):
        u, v, weight = map(int, input().split())
        edges.append(Edge(u, v, weight))

    source = int(input("Введите индекс источника: "))

    bellman_ford(V, E, edges, source)
