from typing import List
from collections import defaultdict


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        """
        Need to validate following things:
            1. There are only two types of lengths
            2. Count of one type should be 4 or 2
        """
        edges = defaultdict(lambda: 0)
        points = [p1, p2, p3, p4]

        def distance(p, q):
            x_dist, y_dist = p[0] - q[0], p[1] - q[1]
            return (x_dist * x_dist) + (y_dist * y_dist)

        for i in range(4):
            for j in range(i + 1, 4):
                dist = distance(points[i], points[j])
                if dist == 0:
                    return False
                edges[dist] += 1

        if len(edges) != 2:
            return False

        firstValue = list(edges.values())[0]
        if firstValue not in (2, 4):
            return False

        return True
