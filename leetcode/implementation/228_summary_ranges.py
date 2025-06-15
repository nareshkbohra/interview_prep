from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        prevStart, prevEnd = nums[0], nums[0]
        for num in nums[1:]:
            if num == prevEnd + 1:
                prevEnd += 1
            else:
                result.append((prevStart, prevEnd))
                prevStart = num
                prevEnd = num
        result.append((prevStart, prevEnd))
        processedResult = []
        for res in result:
            if res[0] == res[1]:
                processedResult.append(str(res[0]))
            else:
                processedResult.append(f"{res[0]}->{res[1]}")
        return processedResult


s = Solution()
nums = [0, 1, 2, 4, 5, 7]
res = s.summaryRanges(nums)
print(res)
