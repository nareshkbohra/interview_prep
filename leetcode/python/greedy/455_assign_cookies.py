from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j = 0, 0
        result = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                result += 1
            j += 1

        return result


sol = Solution()
g = [1, 2, 3]
s = [1, 1]
res = sol.findContentChildren(g, s)
print(res)
