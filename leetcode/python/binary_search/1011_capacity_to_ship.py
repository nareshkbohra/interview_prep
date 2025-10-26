from typing import List


class Solution:
    def countDays(self, weights, shipSize):
        shipCount = 1
        remaining = shipSize
        for weight in weights:
            if weight > remaining:
                shipCount += 1
                remaining = shipSize
            remaining -= weight

        return shipCount

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        minSize = right
        while left <= right:
            mid = (left + right) // 2
            currDays = self.countDays(weights, mid)
            if currDays <= days:
                minSize = mid
                right = mid - 1
            else:
                left = mid + 1

        return minSize


s = Solution()
weights = [1, 2, 3, 1, 1]
days = 4
res = s.shipWithinDays(weights, days)
print(res)
