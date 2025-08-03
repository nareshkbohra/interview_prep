from collections import defaultdict
from typing import List


def print_graph(graph):
    for start, start_value in graph.items():
        for end, curr_cost in start_value.items():
            if curr_cost == float("inf"):
                continue
            print(f"{start} -> {end} = {curr_cost}")


class Solution:
    def build_graph(self, original: List[str], changed: List[str], cost: List[int]):
        graph = defaultdict(lambda: defaultdict(lambda: float("inf")))
        for start, end, change_cost in zip(original, changed, cost):
            if graph[start][end] > change_cost:
                graph[start][end] = change_cost

        for k in range(26):
            k_ch = chr(k + ord("a"))
            for i in range(26):
                i_ch = chr(i + ord("a"))
                for j in range(26):
                    j_ch = chr(j + ord("a"))
                    new_dist = graph[i_ch][k_ch] + graph[k_ch][j_ch]
                    if new_dist < graph[i_ch][j_ch]:
                        graph[i_ch][j_ch] = new_dist

        return graph

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = self.build_graph(original, changed, cost)
        result = 0
        for s_ch, t_ch in zip(source, target):
            if s_ch == t_ch:
                continue
            dist = graph[s_ch][t_ch]
            if dist == float("inf"):
                return -1
            result += int(dist)
        return result


s = Solution()
source = "aaaa"
target = "bbbb"
original = ["a", "c"]
changed = ["c", "b"]
cost = [1, 2]
res = s.minimumCost(source, target, original, changed, cost)
print(res)
