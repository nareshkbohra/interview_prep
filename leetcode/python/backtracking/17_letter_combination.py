from typing import List


class Solution:
    def __init__(self):
        self.map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def helper():
        pass

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        start = self.map[digits[0]]
        remaining = self.letterCombinations(digits[1:])
        if not remaining:
            return start

        result = []
        for s in start:
            for sub_result in remaining:
                result.append(s + sub_result)
        return result


s = Solution()
res = s.letterCombinations("234")
print(res)
