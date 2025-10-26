from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float("inf")] * n for _ in range(n)]
        for i in range(n):
            distance[i][i] = 0
        for start, end, cost in edges:
            distance[start][end] = cost
            distance[end][start] = cost

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        min_neighbor = float("inf")
        result = 0
        for i in range(n):
            neighbors = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    neighbors += 1
            print(f"{i} : {neighbors} {min_neighbor}")
            if neighbors <= min_neighbor:
                min_neighbor = neighbors
                result = i
        return result


n = 4
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
distanceThreshold = 4

s = Solution()
res = s.findTheCity(n, edges, distanceThreshold)
print(res)
