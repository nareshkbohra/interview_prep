from typing import List
from collections import Counter


class Solution:
    def dfs(self, num_counters, index, curr_path, result):
        result.append(list(curr_path))
        for i in range(index, len(num_counters)):
            curr_num, curr_count = num_counters[i]
            for _ in range(curr_count):
                curr_path.append(curr_num)
                self.dfs(num_counters, i + 1, curr_path, result)
            for _ in range(curr_count):
                curr_path.pop()

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        num_counters = [(num, count) for num, count in Counter(nums).items()]
        result = []
        curr_path = []
        self.dfs(num_counters, 0, curr_path, result)
        return result


s = Solution()
nums = [1, 2, 2]
res = s.subsetsWithDup(nums)
print(res)
