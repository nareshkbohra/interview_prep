from typing import List
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        Maintain a sliding window and two queues.
        """
        maxQueue = deque()
        minQueue = deque()
        left = 0
        maxLen = 0
        for right, num in enumerate(nums):
            while maxQueue and num > maxQueue[-1]:
                maxQueue.pop()
            maxQueue.append(num)
            while minQueue and num < minQueue[-1]:
                minQueue.pop()
            minQueue.append(num)
            while maxQueue[0] - minQueue[0] > limit:
                leftNum = nums[left]
                if leftNum == maxQueue[0]:
                    maxQueue.popleft()
                if leftNum == minQueue[0]:
                    minQueue.popleft()
                left += 1
            maxLen = max(maxLen, right - left + 1)

        return maxLen


s = Solution()
nums = [10, 1, 2, 4, 7, 2]
limit = 5
res = s.longestSubarray(nums, limit)
print(res)
