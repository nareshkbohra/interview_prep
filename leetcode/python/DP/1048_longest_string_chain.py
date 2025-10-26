from typing import List
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        memory = defaultdict(lambda: 0)
        words.sort(key=lambda x: len(x))
        for word in words:
            for i in range(len(word)):
                subWord = word[:i] + word[i + 1 :]
                memory[word] = max(memory[word], memory[subWord] + 1)

        return max(memory.values())
