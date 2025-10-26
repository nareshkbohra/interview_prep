from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        reachingOrder = sorted(zip(position, speed), reverse=True)
        maxReachTime = 0
        result = 0
        for currPos, currSpeed in reachingOrder:
            reachTime = (target - currPos) / currSpeed
            if reachTime > maxReachTime:
                maxReachTime = reachTime
                result += 1
        return result


target = 12
position = [10]
speed = [2]
s = Solution()
res = s.carFleet(target, position, speed)
print(res)
