from typing import List
from collections import deque


class Solution:
    def getNeighbors(self, num):
        num = list(num)
        for i in range(4):
            orig = num[i]
            num[i] = (num[i] + 1) % 10
            yield tuple(num)
            num[i] = orig

        for i in range(4):
            orig = num[i]
            num[i] = (num[i] - 1) % 10
            yield tuple(num)
            num[i] = orig

    def openLock(self, deadends: List[str], target: str) -> int:
        if target in deadends:
            return -1

        deadends = set(tuple(int(n) for n in num) for num in deadends)
        target = tuple(int(i) for i in target)
        visited = set()
        queue = deque([(0, 0, 0, 0)])
        steps = 0

        while len(queue):
            queueLen = len(queue)
            for _ in range(queueLen):
                currItem = queue.popleft()
                if currItem == target:
                    return steps
                if currItem in visited or currItem in deadends:
                    continue
                visited.add(currItem)
                for neighbor in self.getNeighbors(currItem):
                    queue.append(neighbor)
            steps += 1
        return -1


s = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
s = Solution()
res = s.openLock(deadends, target)
print(res)
