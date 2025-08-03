from typing import List


class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        hFences.sort()

        vFences.extend([1, n])
        vFences.sort()

        h_dist_set = set()
        for i in range(len(hFences)):
            start = hFences[i]
            for j in range(i + 1, len(hFences)):
                end = hFences[j]
                h_dist_set.add(end - start)

        v_dist_set = set()
        for i in range(len(vFences)):
            start = vFences[i]
            for j in range(i + 1, len(vFences)):
                end = vFences[j]
                v_dist_set.add(end - start)

        common = h_dist_set.intersection(v_dist_set)
        if len(common) == 0:
            return -1

        side = max(common)
        return (side * side) % (10**9 + 7)
