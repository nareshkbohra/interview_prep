from typing import List
from collections import deque
from bisect import bisect_left


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        result = deque()
        left = max(0, bisect_left(arr, x) - 1)
        right = left + 1
        for i in range(k):
            if left >= 0 and right < len(arr):
                if x - arr[left] <= arr[right] - x:
                    result.appendleft(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            else:
                if left >= 0:
                    result.appendleft(arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1
            k += 1

        return list(result)


s = Solution()
arr = [0, 0, 1, 2, 3, 3, 4, 7, 7, 8]
k = 3
x = 5
res = s.findClosestElements(arr, k, x)
print(res)
