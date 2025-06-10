from typing import List, Dict, Tuple
from collections import defaultdict
import heapq
from time import sleep


class Solution:
    def make_graph(self, edges, succProb):
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for (start, end), prob in zip(edges, succProb):
            graph[start].append((end, prob))
            graph[end].append((start, prob))
        return graph

    def maxProbability(
        self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int
    ) -> float:
        graph = self.make_graph(edges, succProb)
        distance = [0] * n
        pq = [(-1, start_node)]
        while len(pq):
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob = -curr_prob
            for neighbor, prob in graph[curr_node]:
                new_prob = curr_prob * prob
                if new_prob > distance[neighbor]:
                    distance[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))

        return distance[end_node]


n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2

s = Solution()
res = s.maxProbability(n, edges, succProb, start, end)
print(res)
