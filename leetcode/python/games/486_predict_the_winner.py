from typing import List


class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, nums, left, right):
        if left > right:
            return 0
        key = (left, right)
        if key in self.memory:
            return self.memory[key]

        leftSum = nums[left] + min(self.helper(nums, left + 2, right), self.helper(nums, left + 1, right - 1))
        rightSum = nums[right] + min(self.helper(nums, left + 1, right - 1), self.helper(nums, left, right - 2))

        result = max(leftSum, rightSum)
        self.memory[key] = result

        return result

    def predictTheWinner(self, nums: List[int]) -> bool:
        playerSum = self.helper(nums, 0, len(nums) - 1)
        return playerSum >= (sum(nums) / 2)


nums = [1, 5, 233, 7]
s = Solution()
res = s.predictTheWinner(nums)
print(res)
