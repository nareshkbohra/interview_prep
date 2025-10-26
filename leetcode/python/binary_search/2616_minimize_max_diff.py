from typing import List


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2
            count = 0

            i = 1
            while i < len(nums):
                diff = nums[i] - nums[i - 1]
                if diff <= mid:
                    i += 1
                    count += 1

                if count == p:
                    break
                i += 1

            if count >= p:
                right = mid
            else:
                left = mid + 1

        return left


nums = [3, 4, 2, 3, 2, 1, 2]
p = 3
s = Solution()
res = s.minimizeMax(nums, p)
print(res)
