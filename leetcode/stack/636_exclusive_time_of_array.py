from typing import List
from collections import deque


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        """
        What we want to do is keep adding time.
        Maintain a stack of running process
        Two things can happend:
            1. start: Check if already a process is running (top of stack).
                a. If not, do not do anything, just push current job with time.
                b. If yes, store the time diff for that job
            2. end: Pop the stack

        """
        lastPid = -1
        result = [0]*n
        stack = deque()
        for log in logs:
            pid, operation, timestamp = log.split(":")
            timestamp = int(timestamp)
            if operation == "start":
                if len(stack):
                    jobId, startTime = stack[-1]
                    result[jobId] += (timestamp-startTime)
                stack.append([int(pid), timestamp])
            else:
                jobId, startTime = stack.pop()
                result[int(jobId)] += (timestamp - startTime+1)
                if len(stack):
                    stack[-1][1] = timestamp+1

        return result

s = Solution()
n = 2
logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
res = s.exclusiveTime(n, logs)
print(res)
