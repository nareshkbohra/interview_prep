from typing import List
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        answer = right
        while left < right:
            mid = (left + right) // 2
            time_taken = sum(ceil(pile / mid) for pile in piles)
            if time_taken > h:
                left = mid + 1
            else:
                answer = mid
                right = mid
        return answer


s = Solution()
piles = [30, 11, 23, 4, 20]
h = 6
res = s.minEatingSpeed(piles, h)
print(res)
