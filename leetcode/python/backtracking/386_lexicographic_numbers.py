from typing import List


class Solution:
    def helper(self, start, n, result):
        if start > n:
            return
        result.append(start)
        for i in range(10):
            next_num = start * 10 + i
            if next_num > n:
                return
            self.helper(next_num, n, result)

    def lexicalOrder(self, n: int) -> List[int]:
        """ """
        result = []
        for i in range(1, 10):
            self.helper(i, n, result)
        return result


s = Solution()
res = s.lexicalOrder(47)
print(res)
