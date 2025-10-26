from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        current_sum = 0
        result = 0
        while right < len(nums):
            current_sum += nums[right]
            while current_sum >= target:
                result = max(result, right - left + 1)
                current_sum -= nums[left]
                left += 1
            right += 1

        return result
