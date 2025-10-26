from typing import List, Dict
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Approach:
            1. Calculate prefix sum for every index
            2. For every value try to find val +- k item.
            3. For all the values which differ by k, get their sum.
        """
        prefix_sum = [0] * len(nums)

        prefix_sum[0] = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]
            prefix_sum[i] = prefix_sum[i - 1] + num

        result = -100_000_000_000_000
        indices: Dict[int, int] = defaultdict(lambda: 100_000_000_000)
        indices[nums[0]] = 0
        for i in range(1, len(nums)):
            num = nums[i]
            num_sum = prefix_sum[i]

            right = num + k
            if right in indices:
                right_index = indices[right]
                current_sum = num_sum - prefix_sum[right_index] + nums[right_index]
                result = max(result, current_sum)
            left = num - k
            if left in indices:
                left_index = indices[left]
                current_sum = num_sum - prefix_sum[left_index] + nums[left_index]
                result = max(result, current_sum)

            if num in indices:
                prev_index = indices[num]
                if prefix_sum[i] < prefix_sum[prev_index]:
                    indices[num] = i
            else:
                indices[num] = i

        if result == -100_000_000_000_000:
            return 0

        return result
