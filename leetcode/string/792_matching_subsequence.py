from typing import List
from collections import defaultdict
import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        charIndexList = defaultdict(list)
        for index, char in enumerate(s):
            charIndexList[char].append(index)

        result = 0
        for word in words:
            lastIndex = -1
            wordFound = True
            for ch in word:
                indices = charIndexList[ch]
                pos = bisect.bisect_right(indices, lastIndex)
                if pos == len(indices):
                    wordFound = False
                    break
                else:
                    lastIndex = indices[pos]

            if wordFound:
                result += 1

        return result


s = Solution()
st = "abcde"
words = ["a", "bb", "acd", "ace"]
res = s.numMatchingSubseq(st, words)
print(res)
