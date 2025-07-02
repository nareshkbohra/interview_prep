from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(lambda: 0)
        counter[0] = 1
        result = 0
        currSum = 0
        for num in nums:
            currSum += num
            result += counter[currSum-k]
            counter[currSum] += 1
        return result
