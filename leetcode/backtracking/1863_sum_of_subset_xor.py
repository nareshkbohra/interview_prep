from typing import List


class Solution:
	def helper(self, nums: List[int], index: int, currXor: int) -> int:
		if index == len(nums):
			return currXor

		return self.helper(nums, index + 1, currXor) + self.helper(nums, index + 1, currXor ^ nums[index])

	def subsetXORSum(self, nums: List[int]) -> int:
		return self.helper(nums, 0, 0)


s = Solution()
res = s.subsetXORSum([5, 1, 6])
print(res)
