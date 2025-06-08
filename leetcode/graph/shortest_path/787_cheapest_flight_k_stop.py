from typing import List, Tuple, Dict
from collections import defaultdict, deque
import sys


class Solution:
    def create_graph(self, flights: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for src, dst, cost in flights:
            graph[src].append((dst, cost))
        return graph

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.create_graph(flights)

        min_distance = [sys.maxsize] * n
        queue = deque([(0, src)])
        steps = 0
        while len(queue) and steps <= k:
            size = len(queue)
            for _ in range(size):
                (curr_cost, curr_node) = queue.popleft()
                for neighbor, cost in graph[curr_node]:
                    new_cost = curr_cost + cost
                    if new_cost < min_distance[neighbor]:
                        queue.append((new_cost, neighbor))
                        min_distance[neighbor] = new_cost
                pass
            steps += 1
        if min_distance[dst] == sys.maxsize:
            return -1
        return min_distance[dst]


n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1

s = Solution()
res = s.findCheapestPrice(n, flights, src, dst, k)
print(res)
