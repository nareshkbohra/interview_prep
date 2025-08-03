from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        if not s:
            return []

        result = [0 for _ in range(len(s))]
        if s[0] == c:
            result[0] = 0
        else:
            result[0] = 1_000_000

        for i in range(1, len(s)):
            if s[i] == c:
                result[i] = 0
            else:
                result[i] = 1 + result[i - 1]

        for i in range(len(s) - 2, -1, -1):
            if s[i] == c:
                continue

            result[i] = min(result[i], 1 + result[i + 1])
        return result
