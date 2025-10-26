from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 1
        while i >= 1:
            if nums[i] > nums[i - 1]:
                break
            i = i - 1

        if i == 0:
            nums.reverse()
            return

        j = i
        while j < len(nums) - 1:
            if nums[j + 1] <= nums[i - 1]:
                break
            j += 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        left, right = i, len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return


s = Solution()
nums = [6, 10, 9, 5]
res = s.nextPermutation(nums)
print(nums)
