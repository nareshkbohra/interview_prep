from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        result = max((i * i + j * j, i * j) for [i, j] in dimensions)
        return result[1]
