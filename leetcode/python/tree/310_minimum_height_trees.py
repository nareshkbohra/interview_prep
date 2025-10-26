from typing import List
from collections import defaultdict, deque


class Solution:
    def bfs(self, start_node, graph):
        visited = set()
        visited.add(start_node)
        parent = {start_node: -1}
        queue = deque([start_node])

        lastNode = None
        while len(queue):
            currNode = queue.popleft()
            lastNode = currNode

            for neighbor in graph[currNode]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)
                parent[neighbor] = currNode

        return lastNode, parent

    def makeGraph(self, edges):
        graph = defaultdict(list)
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        return graph

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        1. Find the diameter of tree.
            a. Pick any node and try to find the farthest node.
            b. Pick that node and again try the farthest node and also the path.
        2. Give middle one/two node as result
        """
        graph = self.makeGraph(edges)
        firstEnd, _ = self.bfs(0, graph)
        secondEnd, parentMap = self.bfs(firstEnd, graph)
        currNode = secondEnd
        path_ = []
        while currNode != -1:
            path_.append(currNode)
            currNode = parentMap[currNode]

        pathLen = len(path_)
        if pathLen % 2 == 1:
            return [path_[pathLen // 2]]

        return [path_[pathLen // 2], path_[pathLen // 2 - 1]]
