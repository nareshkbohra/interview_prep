from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        print(citations)
        i = 0
        while i < len(citations):
            if (i + 1) > citations[i]:
                break
            i += 1
        return i


s = Solution()
citations = [3, 0, 6, 1, 5]
res = s.hIndex(citations)
print(res)
