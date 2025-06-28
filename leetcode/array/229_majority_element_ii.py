from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        result = []
        for item, count in counts.items():
            if count > len(nums) // 3:
                result.append(item)
        return result


s = Solution()
res = s.majorityElement([1, 2])
print(res)
