from typing import List
import sys


class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, nums: List[int], curr_location: int) -> int:
        if curr_location in self.memory:
            return self.memory[curr_location]
        if curr_location == len(nums) - 1:
            return 0

        result = sys.maxsize
        if curr_location >= len(nums):
            return result

        for i in range(1, nums[curr_location] + 1):
            result = min(result, 1 + self.helper(nums, curr_location + i))

        self.memory[curr_location] = result
        return result

    def jump(self, nums: List[int]) -> int:
        self.memory = {}
        return self.helper(nums, 0)


s = Solution()
nums = [2, 3, 0, 1, 4]
res = s.jump(nums)
print(res)
