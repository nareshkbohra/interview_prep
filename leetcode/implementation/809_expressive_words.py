from typing import List


class Solution:
    def convertToCounts(self, s):
        result = []
        prev_ch = s[0]
        prev_count = 1
        for ch in s[1:]:
            if ch == prev_ch:
                prev_count += 1
            else:
                result.append((prev_ch, prev_count))
                prev_ch = ch
                prev_count = 1
        result.append((prev_ch, prev_count))
        return result

    def expressiveWords(self, s: str, words: List[str]) -> int:
        base_counts = self.convertToCounts(s)
        result = 0
        for word in words:
            curr_counts = self.convertToCounts(word)
            if len(curr_counts) != len(base_counts):
                continue

            isValid = True
            for (base_ch, base_count), (curr_ch, curr_count) in zip(base_counts, curr_counts):
                if base_ch != curr_ch:
                    isValid = False
                    break
                if curr_count == base_count:
                    continue

                if curr_count > base_count or base_count < 3:
                    isValid = False
                    break

            if isValid:
                result += 1

        return result


inp = "heeellooo"
words = ["hello", "hi", "helo"]
s = Solution()
res = s.expressiveWords(inp, words)
print(res)
