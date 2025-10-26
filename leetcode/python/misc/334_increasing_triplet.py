from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallestOneCount = float("inf")
        smallestTwoCount = float("inf")
        for num in nums:
            if smallestTwoCount < num:
                return True

            if smallestOneCount < num:
                smallestTwoCount = min(smallestTwoCount, num)
            else:
                smallestOneCount = min(smallestOneCount, num)
        return False


s = Solution()
nums = [2, 1, 5, 0, 4, -1]
res = s.increasingTriplet(nums)
print(res)
