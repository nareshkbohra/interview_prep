from typing import List


class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, n):
        if n not in self.parent:
            self.parent[n] = n
            self.rank[n] = 1
            return n

        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])

        return self.parent[n]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = self.parent[parent_x]
        elif self.rank[parent_y] > self.parent[parent_x]:
            self.parent[parent_x] = self.parent[parent_y]
        else:
            self.parent[parent_x] = self.parent[parent_y]
            self.rank[parent_y] += 1


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        dsu = DSU()
        for row, col in stones:
            dsu.union(row, ~col)

        unique_points = set(dsu.find(i) for i in dsu.parent)
        return len(stones) - len(unique_points)
