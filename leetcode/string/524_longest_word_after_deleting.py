from typing import List


class Solution:
    def isSubsequence(self, s, word):
        i = 0
        j = 0
        while i < len(s):
            if s[i] == word[j]:
                j += 1
                if j == len(word):
                    return True
            i += 1
        return False

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        dictionary.sort()
        result = ""
        for word in dictionary:
            if len(word) <= len(result):
                continue
            if self.isSubsequence(s, word):
                result = word
        return result


inp = "abpcplea"
dictionary = ["ale", "apple", "monkey", "plea"]
s = Solution()
res = s.findLongestWord(inp, dictionary)
print(res)
