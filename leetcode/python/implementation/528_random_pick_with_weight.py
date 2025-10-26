from typing import List
from random import randint
import bisect


class Solution:
    def __init__(self, w: List[int]):
        self.array = [0] * len(w)
        self.array[0] = w[0]
        totalWeight = w[0]

        for i in range(1, len(w)):
            weight = w[i]
            self.array[i] = self.array[i - 1] + weight
            totalWeight += weight

        self.totalWeight = totalWeight

    def pickIndex(self) -> int:
        randWeight = randint(1, self.totalWeight)
        return bisect.bisect_left(self.array, randWeight)
