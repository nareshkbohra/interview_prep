from typing import List
from collections import deque


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        if len(indices) == 0:
            return s

        sorted_indices = deque(sorted((num, index) for index, num in enumerate(indices)))
        result = ""
        i = 0
        while i < len(s):
            curr_s_index, curr_index = sorted_indices.popleft()
            while i != curr_s_index and i < len(s):
                result += s[i]
                i += 1

            # We are here means we need to apply transformation
            if s[i:].startswith(sources[curr_index]):
                result += targets[curr_index]
                i += len(sources[curr_index])

            if len(sorted_indices) == 0:
                result += s[i:]
                break
        return result


inp = "abcd"
indices = [0, 0]
sources = ["a", "b"]
targets = ["b", "c"]

s = Solution()
res = s.findReplaceString(inp, indices, sources, targets)
print(res)
