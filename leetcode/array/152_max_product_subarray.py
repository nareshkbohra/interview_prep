from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        result = -float("inf")
        for num in nums:
            vals = num, num*currMax, num*currMin
            currMax, currMin = max(vals), min(vals)
            result = max(result, currMax)
        return result
