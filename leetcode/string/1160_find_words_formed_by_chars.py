from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_freq = Counter(chars)
        result = 0
        for word in words:
            for ch, freq in Counter(word).items():
                if freq > chars_freq[ch]:
                    break
            else:
                result += len(word)
        return result
