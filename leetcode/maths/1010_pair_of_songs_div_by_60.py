from typing import List, Dict
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count: Dict[int, int] = defaultdict(lambda: 0)
        result = 0
        for t in time:
            t = t % 60
            result += count[60 - t]
            count[t] += 1
        return result
