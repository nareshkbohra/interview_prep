from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        """
        Logic is in two phases:
            1. For every word map it to pattern
            2. Every char should either map to same character
        """
        result = []
        for word in words:
            if len(word) != len(pattern):
                continue
            forward_mapping = {}
            backward_mapping = {}
            for l, r in zip(word, pattern):
                # Both are seen first time, add them
                if l not in forward_mapping and r not in backward_mapping:
                    forward_mapping[l] = r
                    backward_mapping[r] = l
                    continue

                # We are here means atleast one of them has been seen previously
                if r in backward_mapping and backward_mapping[r] != l:
                    break

                if l in forward_mapping and forward_mapping[l] != r:
                    break
            else:
                result.append(word)

        return result


words = ["a", "b", "c"]
pattern = "a"
s = Solution()
res = s.findAndReplacePattern(words, pattern)
print(res)
