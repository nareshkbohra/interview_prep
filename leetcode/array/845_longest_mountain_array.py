from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        increasing = [1] * len(arr)
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                increasing[i] += increasing[i - 1]

        decreasing = [1] * len(arr)
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                decreasing[i] += decreasing[i + 1]

        result = 0
        for i in range(len(arr)):
            if increasing[i] > 1 and decreasing[i] > 1:
                result = max(result, increasing[i] + decreasing[i] - 1)
        return result


s = Solution()
arr = [2, 2, 2]
res = s.longestMountain(arr)
print(res)
