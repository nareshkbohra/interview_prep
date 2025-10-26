from typing import List


class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 1
            return x

        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX == parentY:
            return

        rankX, rankY = self.rank[x], self.rank[y]
        if rankX < rankY:
            self.parent[parentX] = parentY
        elif rankY < rankX:
            self.parent[parentY] = parentX
        else:
            self.parent[parentY] = parentX
            self.rank[parentX] += 1


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()

        result = []
        for start, end in edges:
            if dsu.find(start) == dsu.find(end):
                result = [start, end]
                continue
            dsu.union(start, end)
        return result


s = Solution()
edges = [[1, 2], [1, 3], [2, 3]]
res = s.findRedundantConnection(edges)
print(res)
