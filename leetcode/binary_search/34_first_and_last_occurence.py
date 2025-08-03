from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums, target)
        if left < 0 or left >= len(nums) or nums[left] != target:
            left = -1
        right = bisect_right(nums, target)
        right -= 1
        if right < 0 or right >= len(nums) or nums[right] != target:
            right = -1
        return [left, right]


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
res = s.searchRange(nums, target)
