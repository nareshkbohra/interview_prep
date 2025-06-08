from typing import List, Dict
from collections import namedtuple
import heapq


Node = namedtuple("Node", "x,y")


class DSU:
    def __init__(self):
        self.parent: Dict[Node, Node] = {}
        self.rank: Dict[Node, int] = {}

    def find(self, node: Node) -> Node:
        if node not in self.parent:
            self.parent[node] = node
            self.rank[node] = 1
            return node
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union(self, node_a: Node, node_b: Node):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a == parent_b:
            return
        rank_a = self.rank[node_a]
        rank_b = self.rank[node_b]
        if rank_a > rank_b:
            self.parent[node_b] = node_a
        elif rank_b > rank_a:
            self.parent[node_a] = node_b
        else:
            self.parent[node_a] = node_b
            self.rank[node_b] += 1


class Solution:
    def get_edges(self, points: List[List[int]]):
        edges = []
        for i in range(len(points)):
            (x, y) = points[i]
            start = Node(x, y)
            for j in range(i + 1, len(points)):
                (p, q) = points[j]
                end = Node(p, q)
                distance = abs(end[1] - start[1]) + abs(end[0] - start[0])
                heapq.heappush(edges, (distance, start, end))

        return edges

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.get_edges(points)
        dsu = DSU()
        result = 0
        while len(edges):
            (cost, start, end) = heapq.heappop(edges)
            start_parent = dsu.find(start)
            end_parent = dsu.find(end)
            if start_parent == end_parent:
                continue
            result += cost
            dsu.union(start_parent, end_parent)

        return result


s = Solution()
points = [[0, 0], [2, 2], [3, 10]]
res = s.minCostConnectPoints(points)
print(res)
