class UnionFind:
  def __init__(self, size):
        self.parent = [i for i in range(size)]  
        self.rank = [0] * size  

  
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  
        return self.parent[x]


    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return 

        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1


    def connected(self, x, y):
        return self.find(x) == self.find(y)


    def get_groups(self):
        groups = {}
        for i in range(len(self.parent)):
            root = self.find(i)
            groups.setdefault(root, []).append(i)
        return groups


def test_union_find():
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 3)
    assert uf.connected(1, 4)  
    assert not uf.connected(1, 5) 
    print("Основные тесты пройдены успешно")


def test_performance():
    import time
    uf = UnionFind(100000)
    start = time.time()
    for i in range(1, 100000):
        uf.union(i, i - 1)
    duration = time.time() - start
    print(f"Объединение 100000 элементов завершено за {duration:.2f} секунд")


def display_groups(uf):
    print("Текущие группы:", uf.get_groups())


if __name__ == "__main__":
    uf = UnionFind(10)
    test_union_find()
    display_groups(uf)

    test_performance()
