from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        numWords = len(words)
        result = 0
        for i in range(numWords):
            baseWord = set(words[i])
            for j in range(i + 1, numWords):
                currWord = set(words[j])
                if not baseWord.intersection(currWord):
                    result = max(result, len(words[i]) * len(words[j]))
        return result


s = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
res = s.maxProduct(words)
print(res)

words = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
res = s.maxProduct(words)
print(res)

words = ["a", "aa", "aaa", "aaaa"]
res = s.maxProduct(words)
print(res)
