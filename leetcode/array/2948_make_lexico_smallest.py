from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        sorted_nums = sorted([(nums[i], i) for i in range(n)])
        result = [0] * n

        groups = []
        for i in range(n):
            if i == 0 or sorted_nums[i][0] - sorted_nums[i - 1][0] > limit:
                groups.append([])
            groups[-1].append(sorted_nums[i][1])

        for group in groups:
            sortedGroup = sorted(group)
            for j in range(len(group)):
                result[sortedGroup[j]] = nums[group[j]]

        return result
