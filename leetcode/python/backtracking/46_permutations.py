from typing import List


class Solution:
    def helper(self, nums: List[int], index: int) -> List[List[int]]:
        remaining_nums = len(nums) - index
        if remaining_nums == 0:
            return []
        first_num = nums[index]
        if remaining_nums == 1:
            return [[first_num]]
        sub_results = self.helper(nums, index + 1)
        result = []
        for sub_result in sub_results:
            for i in range(len(sub_result) + 1):
                sub_result_copy = list(sub_result)
                sub_result_copy.insert(i, first_num)
                result.append(sub_result_copy)
        return result

    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper(nums, 0)


s = Solution()
res = s.permute([1, 2, 3])
print(res)
