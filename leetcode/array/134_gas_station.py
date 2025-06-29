from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalGain = 0
        startIndex = 0

        currTank = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            totalGain += diff

            currTank += diff
            if currTank < 0:
                currTank = 0
                startIndex = i + 1

        if totalGain < 0:
            return -1
        return startIndex
