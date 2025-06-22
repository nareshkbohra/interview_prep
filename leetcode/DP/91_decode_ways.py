class Solution:
    def __init__(self):
        self.memory = {}

    def helper(self, s):
        if not s:
            return 1

        key = len(s)
        if key in self.memory:
            return self.memory[key]

        if s[0] == "0":
            return 0
        ways = self.helper(s[1:])
        if len(s) >= 2:
            num = int(s[:2])
            if 10 <= num <= 26:
                ways += self.helper(s[2:])

        self.memory[len(s)] = ways
        return ways

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        self.memory = {}
        return self.helper(s)


s = Solution()
res = s.numDecodings("06")
print(res)
