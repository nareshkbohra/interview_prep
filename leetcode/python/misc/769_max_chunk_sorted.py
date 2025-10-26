from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Every chunk need to have these properties:
        # 1. It should include number i
        # 2. It should have all the element b/w i and j
        result = 0

        i = 0
        while i < len(arr):
            num = i
            numFound = False
            minNumber = num
            maxNumber = num
            j = i
            while j < len(arr):
                minNumber = min(arr[j], minNumber)
                maxNumber = max(arr[j], maxNumber)
                numFound = numFound or arr[j] == num
                if numFound and (maxNumber - minNumber == (j - i)):
                    break
                j += 1
            result += 1
            i = j + 1

        return result


s = Solution()
arr = [1, 0, 2, 3, 4]
res = s.maxChunksToSorted(arr)
print(res)
