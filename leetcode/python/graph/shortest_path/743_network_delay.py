from typing import List, Dict, Tuple
from collections import defaultdict
import heapq


class Solution:
    def make_graph(self, times):
        graph: Dict[int, List[Tuple[int, int]]] = defaultdict(list)
        for start, end, weight in times:
            graph[start].append((end, weight))
        return graph

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distance = [float("inf")] * (n + 1)
        graph = self.make_graph(times)

        distance[k] = 0
        queue = [(0, k)]

        while len(queue):
            (curr_distance, node) = heapq.heappop(queue)
            for neigh, weight in graph[node]:
                new_distance = curr_distance + weight
                if new_distance < distance[neigh]:
                    distance[neigh] = new_distance
                    heapq.heappush(queue, (new_distance, neigh))

        result = max(distance[1:])
        print(distance)
        if result == float("inf"):
            return -1
        return int(result)


s = Solution()
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2
res = s.networkDelayTime(times, n, k)
print(res)
