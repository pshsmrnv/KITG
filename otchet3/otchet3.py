from collections import deque

class Dinic:
    def __init__(self, n):
        self.n = n 
        self.graph = [[] for _ in range(n)]  
        self.level = [-1] * n 
        self.ptr = [0] * n  

    def add_edge(self, u, v, capacity):
        self.graph[u].append([v, capacity, len(self.graph[v])]) 
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])  

    def bfs(self, source, sink):
        queue = deque([source])
        self.level = [-1] * self.n
        self.level[source] = 0
        while queue:
            u = queue.popleft()
            for v, capacity, reverse in self.graph[u]:
                if self.level[v] == -1 and capacity > 0:  
                    self.level[v] = self.level[u] + 1
                    queue.append(v)
                    if v == sink:
                        return True
        return False

    def dfs(self, u, sink, flow):
        if u == sink:
            return flow
        while self.ptr[u] < len(self.graph[u]):
            v, capacity, reverse = self.graph[u][self.ptr[u]]
            if self.level[v] == self.level[u] + 1 and capacity > 0:
                current_flow = min(flow, capacity)
                pushed_flow = self.dfs(v, sink, current_flow)
                if pushed_flow > 0:
                    self.graph[u][self.ptr[u]][1] -= pushed_flow
                    self.graph[v][reverse][1] += pushed_flow
                    return pushed_flow
            self.ptr[u] += 1
        return 0

    def dinic_max_flow(self, source, sink):
        max_flow = 0
        while self.bfs(source, sink): 
            self.ptr = [0] * self.n
            while True:
                flow = self.dfs(source, sink, float('Inf'))
                if flow == 0:
                    break
                max_flow += flow
        return max_flow


if __name__ == "__main__":
    n = 6  
    dinic = Dinic(n)


    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 2, 2)
    dinic.add_edge(1, 3, 5)
    dinic.add_edge(2, 4, 9)
    dinic.add_edge(3, 5, 10)
    dinic.add_edge(4, 5, 10)

    source = 0  
    sink = 5   

    max_flow = dinic.dinic_max_flow(source, sink)
    print("Максимальный поток:", max_flow)
