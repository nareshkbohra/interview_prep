from typing import List


class Solution:
	def __init__(self):
		self.nums = []

	def dfs(self, index: int, curr_path: List[int], result: List[List[int]]):
		result.append(list(curr_path))
		for i in range(index, len(self.nums)):
			curr_path.append(self.nums[i])
			self.dfs(i + 1, curr_path, result)
			curr_path.pop()
		return

	def subsets(self, nums: List[int]) -> List[List[int]]:
		self.nums = nums
		results: List[List[int]] = []
		curr_path = []
		self.dfs(0, curr_path, results)
		return results


s = Solution()
nums = [1, 2]
res = s.subsets(nums)
print(res)
