from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        getNum = {"A": 0, "G": 1, "C": 2, "T": 3}

        baseHash = 0
        result = set()
        for ch in s[:10]:
            num = getNum[ch]
            baseHash = (baseHash * 4) + num

        seen = set()
        seen.add(baseHash)
        for i in range(10, len(s)):
            num = getNum[s[i]]
            baseHash -= getNum[s[i - 10]] * (4**9)
            baseHash = (baseHash * 4) + num
            if baseHash in seen:
                result.add(s[i - 9 : i + 1])
            seen.add(baseHash)

        return list(result)


s = Solution()
st = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
res = s.findRepeatedDnaSequences(st)
print(res)
