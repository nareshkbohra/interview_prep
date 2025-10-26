from typing import List


class Solution:
    def __init__(self):
        self.nums = []
        self.used = []
        self.results = []

    def dfs(self, curr_path: List[int]):
        if len(curr_path) == len(self.nums):
            self.results.append(list(curr_path))
            return

        for i in range(len(self.nums)):
            if self.used[i]:
                continue
            if i > 0 and self.nums[i] == self.nums[i - 1] and not self.used[i - 1]:
                continue
            curr_path.append(self.nums[i])
            self.used[i] = True
            self.dfs(curr_path)
            self.used[i] = False
            curr_path.pop()

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.nums = nums
        self.used = [False] * len(nums)
        curr_path = []
        self.dfs(curr_path)
        return self.results


inums = [1, 1, 2]
s = Solution()
res = s.permuteUnique(inums)
print(res)
