from typing import List
from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        left = Counter(nums)
        end = Counter()
        for num in nums:
            if not left[num]:
                continue
            left[num] -= 1
            if end[num - 1] > 0:
                end[num - 1] -= 1
                end[num] += 1
            elif left[num + 1] > 0 and left[num + 2] > 0:
                left[num + 1] -= 1
                left[num + 2] -= 1
                end[num + 2] += 1
            else:
                return False
        return True


nums = [1, 2, 3, 3, 4, 5]
s = Solution()
res = s.isPossible(nums)
print(res)
