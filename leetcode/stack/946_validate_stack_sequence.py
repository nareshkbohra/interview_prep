from typing import List
from collections import deque


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushQueue = deque([])
        popQueue = deque(popped)
        for num in pushed:
            pushQueue.append(num)
            while len(pushQueue) and len(popQueue):
                if pushQueue[-1] == popQueue[0]:
                    pushQueue.pop()
                    popQueue.popleft()
                else:
                    break

        return len(popQueue) == 0


s = Solution()
pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
res = s.validateStackSequences(pushed, popped)
print(res)
