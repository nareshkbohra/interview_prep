from typing import List, Dict
from collections import defaultdict, deque


class Solution:
    def create_graph(self, connections: List[List[int]]):
        graph: Dict[int, List[int]] = defaultdict(list)
        for start, end in connections:
            graph[start].append(end)
            graph[end].append(start)
        return graph

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        graph = self.create_graph(connections)
        visited = set()
        networks = 0
        for i in range(n):
            if i in visited:
                continue
            networks += 1
            queue = deque([i])
            while len(queue):
                curr_item = queue.pop()
                if curr_item in visited:
                    continue
                visited.add(curr_item)
                for neighbor in graph[curr_item]:
                    queue.append(neighbor)

        total_cables = len(connections)
        cables_needed = n - 1
        if cables_needed > total_cables:
            return -1

        return networks - 1


n = 4
connections = [[0, 1], [0, 2], [1, 2]]
s = Solution()
res = s.makeConnected(n, connections)
print(res)
