from typing import List
from collections import defaultdict


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
                chFound = False
                indices = charIndexList[ch]
                for index in indices:
                    if index > lastIndex:
                        lastIndex = index
                        chFound = True
                        break
                if not chFound:
                    wordFound = False
                    break

            if wordFound:
                result += 1

        return result


s = Solution()
st = "dsahjpjauf"
words = ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]
res = s.numMatchingSubseq(st, words)
print(res)
