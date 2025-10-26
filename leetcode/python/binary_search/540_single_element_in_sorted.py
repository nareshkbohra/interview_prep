from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            """
            First check if atleast one copy of element is present or not
            If not return element at mid.
            If element copy exist, check index of higher one, if it is odd
            Element exist at right else left
            """
            if mid > 0 and nums[mid] == nums[mid - 1]:
                if mid % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 1
                continue

            if mid < len(nums) - 1 and nums[mid] == nums[mid + 1]:
                if (mid + 1) % 2 == 1:
                    left = mid + 1
                else:
                    right = mid - 1
                continue

            return nums[mid]

        return -1


s = Solution()
nums = [3, 3, 7, 7, 10, 11, 11]
res = s.singleNonDuplicate(nums)
print(res)
