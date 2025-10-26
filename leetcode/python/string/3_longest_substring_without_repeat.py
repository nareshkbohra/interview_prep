class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lastOcc = {}
        result = 0
        start = 0
        currLen = 0
        for i in range(len(s)):
            currCh = s[i]
            if currCh in lastOcc and lastOcc[currCh] >= start:
                currLen = i - start
                result = max(result, currLen)
                start = lastOcc[currCh] + 1
            lastOcc[currCh] = i
        result = max(result, len(s) - start)

        return result


inp = "dvdf"
s = Solution()
res = s.lengthOfLongestSubstring(inp)
print(res)
