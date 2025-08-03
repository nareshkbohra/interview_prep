from typing import List


class Solution:
    vowels = {"a", "e", "i", "o", "u"}

    def isValid(self, word):
        return int(word[0] in self.vowels and word[-1] in self.vowels)

    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        counter = [0] * len(words)

        counter[0] = self.isValid(words[0])
        for i in range(1, len(words)):
            counter[i] = counter[i - 1] + self.isValid(words[i])

        result = []
        for [left, right] in queries:
            leftCount, rightCount = counter[left], counter[right]
            isLeftCorrect = self.isValid(words[left])
            result.append(rightCount - leftCount + isLeftCorrect)

        return result
